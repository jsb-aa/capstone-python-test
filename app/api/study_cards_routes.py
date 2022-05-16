from flask import Blueprint
from app.models import Card, db
from vose_sampler import VoseAlias

study_cards_routes = Blueprint('study_cards_routes', __name__)

# GET confidence buckets filled with cards

@study_cards_routes.route('/decks/<int:deckId>')
def study_cards(deckId):
    # Find all the cards in each confidence "bucket"
    not_at_all_cards = Card.query.filter((Card.deck_id == deckId) & ((Card.curr_rating == 0) | (Card.curr_rating == 1))).all()
    hard_cards = Card.query.filter((Card.deck_id == deckId) & ((Card.curr_rating == 2) | (Card.curr_rating == 3))).all()
    easy_cards = Card.query.filter((Card.deck_id == deckId) & (Card.curr_rating == 4)).all()
    perfect_cards = Card.query.filter((Card.deck_id == deckId) & (Card.curr_rating == 5)).all()
    extra_perfect_cards = Card.query.filter((Card.deck_id == deckId) & (Card.curr_rating == 5) & (Card.numFivesInRow == 3)).all()
    
    # Assign different percentages to each card within each bucket
    d_not_at_all = {card: 0.55 for card in not_at_all_cards}
    d_hard = {card: 0.23 for card in hard_cards}
    d_easy = {card: 0.15 for card in easy_cards}
    d_perfect = {card: 0.05 for card in perfect_cards}
    d_extra_perfect = {card: 0.02 for card in extra_perfect_cards}
    
    # Combine all the dictionaries into one "probability distribution", each card having their percentage attached
    d = {**d_not_at_all, **d_hard, **d_easy, **d_perfect, **d_extra_perfect}
    
    # Create the "probability and alias table" that we will take a sampling from; O(n)
    va = VoseAlias(d)
    
    # Initialize the final dictionary to hold the cards
    study_cards = dict()
    
    # Instead of a sample size of 10 automatically, we need to make sure we don't get a repeat card. 
    while len(study_cards) < 10:
        # Returns one card in a list, call to_dict on it to make it readable on front-end
        card = va.sample_n(size=1)[0].to_dict()
        # Now we can compare the ids of the cards & put it in the study_cards dictionary with the id as the key to prevent repeats
        if not card["id"] in study_cards:
            study_cards[card["id"]] = card

    return {"study_cards": list(study_cards.values())} 
    
    
@study_cards_routes.errorhandler(500)
def internal_server_error(e):
    return {"errors": ["Internal Server Error: Study Cards"]}, 500
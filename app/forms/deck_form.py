from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import Deck

def deck_exists(form, field):
    def cb(deck):
        print("hello??", deck.user_id, form.user_id.data)
        if deck.user_id == form.user_id.data:
            return True
        else:
            return False
        
    name = field.data
    decks = Deck.query.filter(Deck.name == name).all()
    result = filter(cb, decks)
    if result:
        raise ValidationError("You already have a deck with this name")

class DeckForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired('Please enter a name for your deck.'), Length(min=2, max=50, message="Deck names must be between 2-50 characters"), deck_exists])
    about = TextAreaField("About", validators=[Length(max=400, message="Deck description must be less than 400 characters")])
    user_id = IntegerField('User Id', validators=[DataRequired()])
    #share = BooleanField("Share?")
    
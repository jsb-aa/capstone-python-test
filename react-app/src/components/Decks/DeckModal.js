import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { Modal } from '../../context/Modal';
import { deleteADeck } from '../../store/decks';
import DeckForm from './DeckForm';

function DeckModal({ type, deck }) {
  const [showModal, setShowModal] = useState(false);
  const [showOptions, setShowOptions] = useState(false);
  const dispatch = useDispatch()

  const handleDelete = () => {
    dispatch(deleteADeck(deck.id, deck))
  }

  const options = (
    <div className='options-container'>
        <div onClick={() => setShowModal(true)} className="edit-deck-button">
              <p>Edit</p>
        </div>
        <div className='delete-deck-button' onClick={handleDelete}>
          <i class="fa-solid fa-trash-can"></i>
        </div>
    </div>
  )

  return (
    <>
        {type === "create" ?
          <div onClick={() => setShowModal(true)} className="create-deck-button">
            <i class="fa-solid fa-plus"></i>
            <p>Create</p>
          </div>
          :
          <>
            <div className='more-options' onClick={() => setShowOptions(true)}>
              <i class="fa-solid fa-ellipsis"></i>
            </div>
            {showOptions && options}

          </>
            }

      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <DeckForm type={type} deck={deck} setShowModal={setShowModal}/>
        </Modal>
      )}
    </>
  );
}

export default DeckModal;
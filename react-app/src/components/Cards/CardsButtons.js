import { useState } from "react"

const CardsButtons = ({ setShowCardsListTab, setShowCreateCardsTab, setHideOverflow }) => {
    const [selected, setSelected] = useState("preview");

    const handlePreviewClick = (e) => {
        e.preventDefault()
        setShowCreateCardsTab(false)
        setShowCardsListTab(true)
        setHideOverflow("auto")
        setSelected("preview")
    }
    
    const handleEditClick = (e) => {
        e.preventDefault()
        setShowCardsListTab(false)
        setShowCreateCardsTab(true)
        setHideOverflow("hidden")
        setSelected("edit")
    }

    return (
        <div className="cards-buttons-container">
            <button className={selected === "preview" ? "selected-button" : "not-selected-button"} onClick={handlePreviewClick}>Preview Cards</button>
            <button className={selected === "edit" ? "selected-button" : "not-selected-button"} onClick={handleEditClick}>Edit Cards</button>
        </div>
    )
}

export default CardsButtons;

const searchInput = document.getElementById("gameSearch");
const gameCards = document.querySelectorAll(".game-card");
const noResults = document.getElementById("noResults");

function searchGames() {
    const searchText = searchInput.value.trim().toLowerCase();
    let visibleGames = 0;

    gameCards.forEach((card) => {
        const gameName = card.querySelector("h3").textContent.toLowerCase();
        const gameCategory = card.querySelector(".game-category").textContent.toLowerCase();
        const gameDescription = card.querySelector(".game-info p").textContent.toLowerCase();

        const matches =
            gameName.includes(searchText) ||
            gameCategory.includes(searchText) ||
            gameDescription.includes(searchText);

        card.style.display = matches ? "" : "none";

        if (matches) {
            visibleGames++;
        }
    });

    noResults.hidden = visibleGames !== 0;
}

searchInput.addEventListener("input", searchGames);

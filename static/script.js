
document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("gameSearch");
    const sortSelect = document.getElementById("sortGames");
    const filterContainer = document.getElementById("categoryFilters");
    const gamesGrid = document.getElementById("gamesGrid");
    const noResults = document.getElementById("noResults");

    // Stop safely if this page doesn't contain the game library.
    if (!searchInput || !sortSelect || !filterContainer || !gamesGrid) {
        return;
    }

    const cards = Array.from(
        gamesGrid.querySelectorAll(".game-card")
    );

    const filterButtons = Array.from(
        filterContainer.querySelectorAll(".filter-button")
    );

    let activeCategory = "all";
    let searchText = "";
    let sortMode = "default";

    // Read saved favourites from this browser.
    function getFavourites() {
        try {
            const saved = JSON.parse(
                localStorage.getItem("nexplay-favourites") || "[]"
            );

            return Array.isArray(saved) ? saved : [];
        } catch (error) {
            return [];
        }
    }

    function saveFavourites(favourites) {
        try {
            localStorage.setItem(
                "nexplay-favourites",
                JSON.stringify(favourites)
            );
        } catch (error) {
            console.warn("NEXPLAY could not save favourites.", error);
        }
    }

    // Update the appearance and accessibility labels of heart buttons.
    function updateFavouriteButtons() {
        const favourites = getFavourites();

        document.querySelectorAll("[data-favorite]").forEach((button) => {
            const isFavourite = favourites.includes(
                button.dataset.favorite
            );

            button.classList.toggle("is-favorite", isFavourite);
            button.setAttribute("aria-pressed", String(isFavourite));
            button.setAttribute(
                "aria-label",
                isFavourite
                    ? "Remove from favourites"
                    : "Add to favourites"
            );
            button.title = isFavourite
                ? "Remove from favourites"
                : "Add to favourites";
            if (button.classList.contains("detail-favorite")) {
    button.textContent = isFavourite
        ? "♥ Remove from Favourites"
        : "♡ Add to Favourites";
} else {
    button.textContent = isFavourite ? "♥" : "♡";
}
        });
    }

    // Search and filter the game library.
    function applyFilters() {
        let visibleCount = 0;

        const sortedCards = [...cards];

        if (sortMode === "az") {
            sortedCards.sort((a, b) =>
                a.dataset.name.localeCompare(b.dataset.name)
            );
        } else if (sortMode === "za") {
            sortedCards.sort((a, b) =>
                b.dataset.name.localeCompare(a.dataset.name)
            );
        }

        // Reorder cards without recreating them.
        sortedCards.forEach((card) => gamesGrid.appendChild(card));

        sortedCards.forEach((card) => {
            const nameMatches = card.dataset.name.includes(searchText);

            const categoryMatches =
                activeCategory === "all" ||
                card.dataset.category === activeCategory;

            const isVisible = nameMatches && categoryMatches;

            card.hidden = !isVisible;

            if (isVisible) {
                visibleCount++;
            }
        });

        if (noResults) {
            noResults.hidden = visibleCount !== 0;
        }
    }

    // Search as the user types.
    searchInput.addEventListener("input", () => {
        searchText = searchInput.value.trim().toLowerCase();
        applyFilters();
    });

    // Filter by category.
    filterButtons.forEach((button) => {
        button.addEventListener("click", () => {
            activeCategory = button.dataset.category || "all";

            filterButtons.forEach((item) => {
                item.classList.toggle("active", item === button);
            });

            applyFilters();
        });
    });

    // Sort alphabetically.
    sortSelect.addEventListener("change", () => {
        sortMode = sortSelect.value;
        applyFilters();
    });

    // Add or remove a favourite.
    document.addEventListener("click", (event) => {
        const button = event.target.closest("[data-favorite]");

        if (!button) {
            return;
        }

        const slug = button.dataset.favorite;

        if (!slug) {
            return;
        }

        const favourites = getFavourites();
        const index = favourites.indexOf(slug);

        if (index >= 0) {
            favourites.splice(index, 1);
        } else {
            favourites.push(slug);
        }

        saveFavourites(favourites);
        updateFavouriteButtons();
    });

    // Initialise the page.
    updateFavouriteButtons();
    applyFilters();
});

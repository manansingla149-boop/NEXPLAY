
document.addEventListener("DOMContentLoaded", () => {
    const root = document.documentElement;

    const themes = {
        purple: "#a855f7",
        blue: "#3b82f6",
        green: "#22c55e"
    };

    let savedTheme = "purple";

    try {
        const storedTheme = localStorage.getItem("nexplay-theme");

        if (storedTheme && themes[storedTheme]) {
            savedTheme = storedTheme;
        }
    } catch (error) {
        console.warn("NEXPLAY could not load the saved theme.");
    }

    function applyTheme(themeName) {
        if (!themes[themeName]) return;

        root.style.setProperty("--nexplay-accent", themes[themeName]);

        try {
            localStorage.setItem("nexplay-theme", themeName);
        } catch (error) {
            console.warn("NEXPLAY could not save the theme.");
        }

        document.querySelectorAll("[data-nexplay-theme]").forEach(button => {
            const selected = button.dataset.nexplayTheme === themeName;

            button.setAttribute("aria-pressed", String(selected));
        });
    }

    document.querySelectorAll("[data-nexplay-theme]").forEach(button => {
        button.addEventListener("click", () => {
            applyTheme(button.dataset.nexplayTheme);
        });
    });

    applyTheme(savedTheme);

    console.log("NEXPLAY theme system ready!");
});

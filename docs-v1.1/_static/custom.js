// Set dark mode as default if no preference is stored
(function() {
    const storedTheme = localStorage.getItem("theme");
    if (!storedTheme) {
        // No stored preference - set dark as default
        document.body.dataset.theme = "dark";
        localStorage.setItem("theme", "dark");
    }
})();

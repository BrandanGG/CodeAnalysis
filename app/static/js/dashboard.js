document.addEventListener('DOMContentLoaded', function () {
    // Toggle user menu
    const toggleButton = document.getElementById('usersettings');
    const menu = document.getElementById('usermenu');

    toggleButton.addEventListener('click', () => {
        menu.classList.toggle('hidden'); // Toggles the 'hidden' class to show/hide the menu
    });

    // Custom file input message
    const fileInput = document.getElementById('fileInput');
    if (fileInput) { // Ensure elements exist before adding event listeners
        fileInput.addEventListener('change', function() {
            fileLabel.textContent = "Upload File";
        });
    }
});

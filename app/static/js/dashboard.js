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

    // hide flashed messages
    setTimeout(function() {
        const flashes = document.querySelectorAll('.flash');
        flashes.forEach(flash => flash.classList.add('hidden'));
    }, 3000); // hide after 3 seconds
});

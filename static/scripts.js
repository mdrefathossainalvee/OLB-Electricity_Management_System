// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Example: Alert on form submission
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const confirmation = confirm("Are you sure you want to submit this form?");
            if (!confirmation) {
                event.preventDefault(); // Prevent form submission
            }
        });
    });

    // Example: Toggle visibility of elements
    const toggleButtons = document.querySelectorAll('.toggle-button');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.classList.toggle('hidden');
            }
        });
    });
});
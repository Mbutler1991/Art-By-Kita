if (!localStorage.getItem('cookiesAccepted')) {
    document.getElementById('cookie-consent-banner').style.display = 'block';
}

// Accept cookies and hide the banner
document.getElementById('accept-cookies').addEventListener('click', function () {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookie-consent-banner').style.display = 'none';
});

// Code to make newsletter tab work
document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementById('newsletter-toggle');
    const formContainer = document.getElementById('newsletter-signup-tab');

    toggleButton.addEventListener('click', function () {
        formContainer.classList.toggle('open');
    });
});
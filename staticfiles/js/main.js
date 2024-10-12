if (!localStorage.getItem('cookiesAccepted')) {
    document.getElementById('cookie-consent-banner').style.display = 'block';
}

// Accept cookies and hide the banner
document.getElementById('accept-cookies').addEventListener('click', function () {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookie-consent-banner').style.display = 'none';
});
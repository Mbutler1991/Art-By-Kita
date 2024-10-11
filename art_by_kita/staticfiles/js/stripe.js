$(document).ready(function() {
    // Initialize Stripe with your public key
    var stripe = Stripe(STRIPE_PUBLIC_KEY);  // Corrected 'Stripe' with uppercase 'S'
    var elements = stripe.elements();

    // Create an instance of the card Element
    var card = elements.create('card');
    card.mount('#card-element');

    // Handle form submission
    var form = document.getElementById('payment-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        stripe.confirmCardPayment(CLIENT_SECRET, {
            payment_method: {
                card: card,
            }
        }).then(function(result) {
            if (result.error) {
                // Display error message in #card-errors
                document.getElementById('card-errors').textContent = result.error.message;
            } else {
                // The payment has been processed
                if (result.paymentIntent.status === 'succeeded') {
                    // Redirect to success page
                    window.location.href = SUCCESS_URL;
                }
            }
        });
    });
});


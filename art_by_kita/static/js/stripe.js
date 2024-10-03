
  var stripe = Stripe("{{ stripe_public_key }}");

  var submitButton = document.getElementById("submit-payment");

  submitButton.addEventListener("click", function() {
    stripe.confirmCardPayment("{{ client_secret }}", {
      payment_method: {
        card: {
          // Assuming you have a card element in your form
          number: document.getElementById('card_number'),
          exp_month: document.getElementById('exp_month'),
          exp_year: document.getElementById('exp_year'),
          cvc: document.getElementById('cvc')
        },
        billing_details: {
          name: document.getElementById('cardholder_name').value,
        }
      }
    }).then(function(result) {
      if (result.error) {
        // Show error to your customer
        console.error(result.error.message);
      } else {
        // The payment has been processed!
        if (result.paymentIntent.status === 'succeeded') {
          // Redirect to a success page
          window.location.href = "{% url 'order_success' order.id %}";
        }
      }
    });
  });


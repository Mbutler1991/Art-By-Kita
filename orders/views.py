from django.shortcuts import get_object_or_404, redirect, render
import stripe
from django.conf import settings
from django.contrib import messages
import logging
from basket.models import Basket, BasketItem
from gallery.models import Painting
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)


@login_required
def create_order(request):
    if request.method == 'POST':
        # Get or create the user's basket
        basket, created = Basket.objects.get_or_create(user=request.user)

        # Check if there's a painting ID in the request (e.g., from the "Purchase" button)
        painting_id = request.POST.get('painting_id')
        if painting_id:
            painting = get_object_or_404(Painting, id=painting_id)
            basket_item, item_created = BasketItem.objects.get_or_create(
                basket=basket,
                painting=painting,
                defaults={'quantity': 1}
            )
            if not item_created:
                basket_item.quantity += 1
                basket_item.save()

        # Ensure there are items in the basket
        if not basket.items.exists():
            messages.error(request, 'No paintings selected for this order.')
            return redirect('gallery:painting_list')  # Or any appropriate page

        # Create the order
        order = Order.objects.create(
            user=request.user,
            full_name=f"{request.user.first_name} {request.user.last_name}",
            email=request.user.email,
            phone_number=request.user.phone_number,
            address=request.user.shipping_address,
            total_amount=0,
        )

        total_amount = 0

        for item in basket.items.all():
            quantity = item.quantity
            total_amount += item.painting.price * quantity

            OrderItem.objects.create(
                order=order,
                painting=item.painting,
                quantity=quantity,
                price=item.painting.price
            )

        # Update order total amount
        order.total_amount = total_amount
        order.save()

        # Validate minimum amount
        MINIMUM_AMOUNT_EUR_CENTS = 25  # 0.25 EUR
        amount_cents = int(round(total_amount * 100))

        if amount_cents < MINIMUM_AMOUNT_EUR_CENTS:
            messages.error(request, "The total amount is below the minimum chargeable amount (0.25 EUR). Please add more items to your order.")
            order.delete()
            return redirect('basket:view_basket')

        try:
            # Create Stripe Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=amount_cents,
                currency='eur',
                metadata={'order_id': order.id}
            )
        except stripe.error.StripeError as e:
            logger.error(f"Stripe Error: {e.user_message}")
            messages.error(
                request, "There was an error processing your payment. Please try again.")
            order.delete()
            return redirect('basket:view_basket')

        order.stripe_payment_intent = intent['id']
        order.save()

        context = {
            'order': order,
            'client_secret': intent['client_secret'],
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'full_name': order.full_name,
            'email': order.email,
            'phone_number': order.phone_number,
            'address': order.address,
        }

        return render(request, 'orders/payment.html', context)

    return redirect('home:home')


def order_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    # Retrieve the Payment Intent from Stripe
    payment_intent = stripe.PaymentIntent.retrieve(order.stripe_payment_intent)

    if payment_intent.status == 'succeeded':
        # Update order status to completed
        order.status = 'Completed'
        order.save()
        return render(request, 'orders/success.html', {'order': order})

    # If payment did not succeed send to cancel screen instead
    return redirect('order_cancel')


def order_cancel(request):
    return render(request, 'orders/cancel.html')

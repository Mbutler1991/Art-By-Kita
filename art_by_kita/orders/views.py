import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from gallery.models import Painting

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_order(request, painting_id):
    painting = get_object_or_404(Painting, pk=painting_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        total_amount = painting.price * quantity

        # Create Order
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            total_amount=total_amount
        )

        # Create OrderItem
        OrderItem.objects.create(
            order=order,
            painting=painting,
            quantity=quantity,
            price=painting.price
        )

        # Create Stripe Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),  # Amount in cents
            currency='usd',
            metadata={'order_id': order.id}
        )

        order.stripe_payment_intent = intent['id']
        order.save()

        context = {
            'order': order,
            'client_secret': intent['client_secret'],
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        }

        return render(request, 'orders/payment.html', context)

    context = {
        'painting': painting
    }

    return render(request, 'orders/create_order.html', context)

def order_success(request, order_id):
    order = get_object_or_404(Order, pk=order_id)

    # Retrieve the Payment Intent from Stripe
    payment_intent = stripe.PaymentIntent.retrieve(order.stripe_payment_intent)

    if payment_intent.status == 'succeeded':
        # Update order status or perform other actions
        order.status = 'Completed'
        order.save()
        return render(request, 'orders/success.html', {'order': order})
    
    # If payment did not succeed, handle it accordingly
    return redirect('order_cancel')

def order_cancel(request):
    return render(request, 'orders/cancel.html')
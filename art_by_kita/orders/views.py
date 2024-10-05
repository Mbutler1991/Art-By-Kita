from django.shortcuts import get_object_or_404, redirect, render
from .models import Order, OrderItem
from .models import Painting  
import stripe
from django.conf import settings

def create_order(request):
    if request.method == 'POST':
        # Get the painting IDs from the POST request
        painting_ids = request.POST.getlist('painting_ids')  

        # Create an order
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            total_amount=0,  
        )

        total_amount = 0 

        for painting_id in painting_ids:
            painting = get_object_or_404(Painting, pk=painting_id)
            quantity = int(request.POST.get(f'quantity_{painting_id}', 1))  
            total_amount += painting.price * quantity  

            # Create OrderItem for each painting
            OrderItem.objects.create(
                order=order,
                painting=painting,
                quantity=1,
                price=painting.price
            )

        # Update the order total amount after adding all items
        order.total_amount = total_amount
        order.save()

        # Create Stripe Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),  
            currency='eur',
            metadata={'order_id': order.id}
        )

        order.stripe_payment_intent = intent['id']
        order.save()

        context = {
            'order': order,
            'client_secret': intent['client_secret'],
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
            'full_name': request.user.full_name if request.user.is_authenticated else '',
            'email': request.user.email if request.user.is_authenticated else '',
            'phone_number': request.user.phone_number if request.user.is_authenticated else '',
            'address': request.user.address if request.user.is_authenticated else '',
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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from gallery.models import Painting
from .models import Basket, BasketItem
from django.contrib import messages

@login_required
def view_basket(request):
    basket, created = Basket.objects.get_or_create(user=request.user)
    items = basket.items.select_related('painting')
    total_cost = basket.get_total_cost()
    context = {
        'basket': basket,
        'items': items,
        'total_cost': total_cost,
    }
    return render(request, 'basket/view_basket.html', context)

@login_required
def add_to_basket(request, painting_id):
    painting = get_object_or_404(Painting, pk=painting_id)
    basket, created = Basket.objects.get_or_create(user=request.user)
    basket_item, created = BasketItem.objects.get_or_create(basket=basket, painting=painting)
    
    if not created:
        basket_item.quantity += 1
        basket_item.save()
        messages.info(request, f'Increased quantity of {painting.name} in your basket.')
    else:
        messages.success(request, f'Added {painting.name} to your basket.')
    
    return redirect('basket:view_basket')

@login_required
def remove_from_basket(request, item_id):
    basket = get_object_or_404(Basket, user=request.user)
    basket_item = get_object_or_404(BasketItem, pk=item_id, basket=basket)
    basket_item.delete()
    messages.success(request, f'Removed {basket_item.painting.name} from your basket.')
    return redirect('basket:view_basket')

@login_required
def update_basket_item(request, item_id):
    if request.method == 'POST':
        basket = get_object_or_404(Basket, user=request.user)
        basket_item = get_object_or_404(BasketItem, pk=item_id, basket=basket)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            basket_item.quantity = quantity
            basket_item.save()
            messages.success(request, f'Updated quantity for {basket_item.painting.name}.')
        else:
            basket_item.delete()
            messages.success(request, f'Removed {basket_item.painting.name} from your basket.')
    
    return redirect('basket:view_basket')

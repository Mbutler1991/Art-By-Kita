from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('painting', 'quantity', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_amount', 'stripe_payment_intent')
    search_fields = ('id', 'user_username', 'stripe_payment_intent')
    list_filter = ['created_at']
    inlines = [OrderItemInline]


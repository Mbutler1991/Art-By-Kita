from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        'username', 'email', 'first_name',
        'last_name', 'shipping_address',
        'country_code', 'phone_number'
        )
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {'fields': (
                'shipping_address', 'country_code', 'phone_number'
                )}
            ),
    )


admin.site.register(CustomUser, CustomUserAdmin)

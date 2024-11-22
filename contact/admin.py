from django.contrib import admin
from django.contrib import messages
from .models import Contact
from .forms import ContactForm


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created_at']
    list_filter = ['created_at']

    form = ContactForm

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            return readonly_fields + ['name', 'email', 'message', 'created_at']  
        return readonly_fields


admin.site.register(Contact, ContactAdmin)

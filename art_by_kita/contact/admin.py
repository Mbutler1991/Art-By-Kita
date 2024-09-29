from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.html import format_html
from .models import Contact
from .forms import ContactReplyForm
from django import forms


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created', 'reply_button']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'created']
    list_filter = ['created']

    form = ContactReplyForm

    def reply_button(self, obj):
        return format_html('<a class="button" href="{}">Reply</a>', obj.id)
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if 'reply_message' in form.cleaned_data and form.cleaned_data['reply_message']:
            reply_message = form.cleaned_data['reply_message']
            subject = f"Reply to your message from Art by Kita"
            recipient_email = obj.email
            try:
                send_mail(
                    subject,
                    reply_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [recipient_email],
                    fail_silently=False
                )
                messages.success(request, 'The reply was successfully sent.')
            except Exception as e:
                messages.error(request, f'The reply could not be sent. Error: {e}')

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj:
            return readonly_fields + ['name', 'email', 'message', 'created']
        return readonly_fields

admin.site.register(Contact, ContactAdmin)
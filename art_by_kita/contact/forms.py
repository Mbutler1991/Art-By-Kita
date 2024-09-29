from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'})
        }

class ContactReplyForm(forms.ModelForm):
    reply_message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Reply Message'}), required=False)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'reply_message']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
            'message': forms.Textarea(attrs={'readonly': 'readonly'}),
        }
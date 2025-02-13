from django import forms
from .models import Contact
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

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
        captcha = ReCaptchaField(widget=ReCaptchaV3())

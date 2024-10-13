from django import forms

class NewsletterSignupForm(forms.Form):
    email = forms.EmailField(label='Your Email', max_length=100, widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email',
        'class': 'form-control'
    }))
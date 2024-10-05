from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(forms.ModelForm):
    full_name = forms.CharField(max_length=255)
    shipping_address = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Add other fields as necessary

    def save(self, commit=True):
        user = super().save(commit)
        UserProfile.objects.create(
            user=user,
            full_name=self.cleaned_data['full_name'],
            shipping_address=self.cleaned_data['shipping_address'],
            phone_number=self.cleaned_data['phone_number']
        )
        return user
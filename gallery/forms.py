from django import forms
from .models import Painting


class PaintingForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = [
            'title', 'description', 'dimensions', 'materials', 'image', 'price'
            ]
        
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

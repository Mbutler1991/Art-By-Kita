from django import forms

class ReplyForm(forms.Form):
    reply = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), label="Reply Message")

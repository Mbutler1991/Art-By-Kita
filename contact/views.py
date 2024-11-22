from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],  
            )
            contact.save()
            return redirect('contact:thank_you') 
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def thank_you_view(request):
    return render(request, 'contact/thank_you.html')

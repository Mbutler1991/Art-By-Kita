from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.customer = request.user  
            contact.save()
            return redirect('contact:thank_you')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def thank_you_view(request):
    return render(request, 'contact/thank_you.html')


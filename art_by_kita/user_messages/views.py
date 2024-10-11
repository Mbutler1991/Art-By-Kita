from django.shortcuts import render, redirect, get_object_or_404
from .models import UserMessage
from django.contrib.auth.decorators import login_required
from contact.models import Contact

@login_required
def staff_inbox(request):
    chats = Contact.objects.all()  
    return render(request, 'user_messages/staff_inbox.html', {'chats': chats})

@login_required
def message_detail(request, pk):
    chat = get_object_or_404(Contact, pk=pk) 
    return render(request, 'user_messages/message_detail.html', {'chat': chat})

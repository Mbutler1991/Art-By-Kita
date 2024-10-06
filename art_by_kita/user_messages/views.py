from django.shortcuts import render, redirect, get_object_or_404
from .models import UserMessage
from django.contrib.auth.decorators import login_required
from contact.models import Contact 

@login_required
def customer_inbox(request):
    if request.user.is_staff:
        return redirect('user_messages:staff_inbox.html')  

    messages = UserMessage.objects.filter(customer=request.user)
    return render(request, 'user_messages/customer_inbox.html', {'messages': messages})

@login_required
def staff_inbox(request):
    if not request.user.is_staff:
        return redirect('user_messages:customer_inbox')  

    chats = Contact.objects.all()  
    return render(request, 'user_messages/staff_inbox.html', {'chats': chats})

@login_required
def reply_to_message(request, message_id):
    message = get_object_or_404(UserMessage, id=message_id)

    if request.method == 'POST':
        reply = request.POST.get('reply')
        message.reply = reply
        message.staff = request.user
        message.save()
        return redirect('user_messages:staff_inbox')

    return render(request, 'user_messages/reply_to_message.html', {'message': message})

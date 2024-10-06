from django.shortcuts import render, redirect, get_object_or_404
from .models import UserMessage
from django.contrib.auth.decorators import login_required
from contact.models import Contact 
from .forms import ReplyForm  

@login_required
def customer_inbox(request):
    if request.user.is_staff:
        return redirect('user_messages:staff_inbox.html')  

    chats = UserMessage.objects.filter(customer=request.user)
    return render(request, 'user_messages/customer_inbox.html', {'chats': chats})

@login_required
def staff_inbox(request):
    if not request.user.is_staff:
        return redirect('user_messages:customer_inbox')  

    chats = Contact.objects.all()  
    return render(request, 'user_messages/staff_inbox.html', {'chats': chats})

@login_required
def reply_to_message(request, message_id):
    chat = get_object_or_404(UserMessage, id=message_id)

    if request.method == 'POST':
        reply = request.POST.get('reply')
        chat.reply = reply
        chat.staff = request.user
        chat.save()
        return redirect('user_messages:staff_inbox')

    return render(request, 'user_messages/reply_to_message.html', {'chat': chat})

def message_detail(request, pk):
    chat = get_object_or_404(Contact, pk=pk)
    return render(request, 'user_messages/message_detail.html', {'chat': chat})

def message_reply(request, pk):
   chat = get_object_or_404(Contact, pk=pk)
    
   if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            # Save the reply to the message
            chat.reply_message = form.cleaned_data['reply']
            chat.save()
            return redirect('user_messages:staff_inbox')
   else:
       form = ReplyForm()
    
   return render(request, 'user_messages/message_reply.html', {'chat': chat, 'form': form})
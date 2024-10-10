from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomUserUpdateForm  
from django.contrib.auth.decorators import login_required
from .models import CustomUser 
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home:home') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    custom_user = CustomUser.objects.get(id=request.user.id)  
    return render(request, 'accounts/profile.html', {'profile': custom_user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('accounts:profile')  
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def profile_delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  
        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('home:home') 
    return render(request, 'accounts/profile_delete.html')
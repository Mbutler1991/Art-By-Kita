from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm  
from django.contrib.auth.decorators import login_required
from .models import CustomUser 

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('home:home')  # Redirect to the home page or any other page
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    custom_user = CustomUser.objects.get(id=request.user.id)  
    return render(request, 'accounts/profile.html', {'profile': custom_user})
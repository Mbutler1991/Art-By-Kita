from django.shortcuts import render
from datetime import datetime

def home_view(request):
    return render(request, 'home/home.html', {'current_date': datetime.now()})

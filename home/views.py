from django.shortcuts import render
from datetime import datetime
from gallery.models import Painting
import random


def home_view(request):
    paintings = Painting.objects.all()
    random_painting = random.choice(paintings) if paintings else None

    context = {
        'random_painting': random_painting,
    }
    
    return render(request, 'home/home.html', context)

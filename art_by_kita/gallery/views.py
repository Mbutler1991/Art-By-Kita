from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Painting

class PaintingListView(ListView):
    model = Painting
    template_name = 'gallery/painting_list.html'
    context_object_name = 'paintings'
    paginate_by = 10

class PaintingDetailView(DetailView):
    model = Painting
    template_name = 'gallery/painting_detail.html'
    context_object_name = 'painting'

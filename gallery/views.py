from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Painting
from .forms import PaintingForm


class PaintingListView(ListView):
    model = Painting
    template_name = 'gallery/painting_list.html'
    context_object_name = 'paintings'
    paginate_by = 10


class PaintingDetailView(DetailView):
    model = Painting
    template_name = 'gallery/painting_detail.html'
    context_object_name = 'painting'


@login_required
def basket(request):
    # Your basket logic here
    return render(request, 'orders/basket.html')


def staff_required(login_url=None):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)


@login_required
@staff_required(login_url='login')  # Redirect to login if not staff
def manage_paintings(request):
    paintings = Painting.objects.all()
    return render(
        request, 'gallery/manage_paintings.html', {'paintings': paintings}
        )


@login_required
@staff_required(login_url='login')
def create_painting(request):
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Painting created successfully.')
            return redirect('gallery:manage_paintings')
    else:
        form = PaintingForm()
    return render(request, 'gallery/create_painting.html', {'form': form})


@login_required
@staff_required(login_url='login')
def edit_painting(request, painting_id):
    painting = get_object_or_404(Painting, pk=painting_id)
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.save()
            messages.success(request, 'Painting updated successfully.')
            return redirect('gallery:manage_paintings')
    else:
        form = PaintingForm(instance=painting)
    return render(
        request, 'gallery/edit_painting.html', {'form': form, 'painting': painting}
        )


@login_required
@staff_required(login_url='login')
def delete_painting(request, painting_id):
    painting = get_object_or_404(Painting, pk=painting_id)
    if request.method == 'POST':
        painting.delete()
        messages.success(request, 'Painting deleted successfully.')
        return redirect('gallery:manage_paintings')
    return render(
        request, 'gallery/delete_painting.html', {'painting': painting}
        )

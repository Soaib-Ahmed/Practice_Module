from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Musician
from .forms import MusicianForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
# def add_musician(request):
#     if request.method == 'POST':
#         musician_form = forms.MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('add_musician')
#     else:
#         musician_form = forms.MusicianForm()

#     return render(request, 'add_musician.html', {'form': musician_form})

class MusicianListView(ListView):
    model = Musician
    template_name = 'musician_list.html'

@method_decorator(login_required,name='dispatch')
class MusicianCreateView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')

# def edit_musician(request, musician_id):
#     musician = get_object_or_404(Musician, pk=musician_id)
#     musician_form = forms.MusicianForm(instance=musician)

#     if request.method == 'POST':
#         musician_form = forms.MusicianForm(request.POST, instance=musician)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('homepage')

#     return render(request, 'edit_musician.html', {'form': musician_form, 'musician': musician})

@method_decorator(login_required,name='dispatch')
class MusicianUpdateView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'edit_musician.html'
    success_url = reverse_lazy('homepage')

# def delete_musician(request, musician_id):
#     musician = get_object_or_404(Musician, pk=musician_id)
#     musician.delete()
#     return redirect('homepage')

@method_decorator(login_required,name='dispatch')
class MusicianDeleteView(DeleteView):
    model = Musician
    success_url = reverse_lazy('homepage')
    template_name = 'musician_confirm_delete.html'
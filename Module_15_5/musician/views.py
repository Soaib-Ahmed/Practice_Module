from django.shortcuts import render,redirect ,get_object_or_404
from . import forms
from .models import Musician

# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form = forms.MusicianForm()

    return render(request, 'add_musician.html', {'form': musician_form})


def edit_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    musician_form = forms.MusicianForm(instance=musician)

    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')

    return render(request, 'edit_musician.html', {'form': musician_form, 'musician': musician})


def delete_musician(request, musician_id):
    musician = get_object_or_404(Musician, pk=musician_id)
    musician.delete()
    return redirect('homepage')
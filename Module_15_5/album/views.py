from django.shortcuts import render,redirect, get_object_or_404
from . import forms
from .models import Album
from .forms import AlbumForm

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()

    return render(request, 'add_album.html', {'form': album_form})



def edit_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    album_form = AlbumForm(instance=album)

    if request.method == 'POST':
        album_form = AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')

    return render(request, 'edit_album.html', {'form': album_form, 'album': album})
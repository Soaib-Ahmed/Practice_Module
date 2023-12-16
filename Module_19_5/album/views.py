from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Album
from .forms import AlbumForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
# def add_album(request):
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('add_album')
#     else:
#         album_form = forms.AlbumForm()

#     return render(request, 'add_album.html', {'form': album_form})

@method_decorator(login_required,name='dispatch')
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        return super().form_valid(form)



# def edit_album(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     album_form = AlbumForm(instance=album)

#     if request.method == 'POST':
#         album_form = AlbumForm(request.POST, instance=album)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('homepage')

#     return render(request, 'edit_album.html', {'form': album_form, 'album': album})

@method_decorator(login_required,name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'
    pk_url_kwarg = 'album_id'  # Change to the actual keyword argument used in your URL
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        # Customize this method if you need to perform additional actions
        return super().form_valid(form)

    def get_object(self, queryset=None):
        # Override this method to customize how you get the object based on the URL parameters
        album_id = self.kwargs.get(self.pk_url_kwarg)
        return get_object_or_404(Album, pk=album_id)
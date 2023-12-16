from django.urls import path
from .views import AddAlbumView, EditAlbumView

#app_name = 'albums'
# urlpatterns = [
#     path('add/',views.add_album, name='add_album'),

#     path('edit/<int:album_id>/', views.edit_album, name='edit_album'),
# ]
urlpatterns = [
    path('add_album/', AddAlbumView.as_view(), name='add_album'),
    path('edit_album/<int:album_id>/', EditAlbumView.as_view(), name='edit_album'),
]
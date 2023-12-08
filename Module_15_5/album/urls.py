from django.urls import path,include
from .import views

#app_name = 'albums'
urlpatterns = [
    path('add/',views.add_album, name='add_album'),

    path('edit/<int:album_id>/', views.edit_album, name='edit_album'),
]
from django.urls import path
from .views import MusicianListView, MusicianCreateView, MusicianUpdateView, MusicianDeleteView


# urlpatterns = [
#     path('add/',views.add_musician, name='add_musician'),
#     path('edit/<int:musician_id>/', views.edit_musician, name='edit_musician'),
#     path('delete/<int:musician_id>/', views.delete_musician, name='delete_musician'),
# ]

urlpatterns = [
    # path('musician/', MusicianListView.as_view(), name='musician_list'),
    path('musician/add/', MusicianCreateView.as_view(), name='add_musician'),
    path('musician/<int:pk>/edit/', MusicianUpdateView.as_view(), name='edit_musician'),
    path('musician/<int:pk>/delete/', MusicianDeleteView.as_view(), name='delete_musician'),
]

from django.urls import path,include
from .import views


urlpatterns = [
    path('add/',views.add_musician, name='add_musician'),
    path('edit/<int:musician_id>/', views.edit_musician, name='edit_musician'),
    path('delete/<int:musician_id>/', views.delete_musician, name='delete_musician'),
]
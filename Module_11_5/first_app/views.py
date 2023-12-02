from django.shortcuts import render
from .meals_data import meals 

# Create your views here.
def index(request):
    return render(request, 'index.html', {'meals': meals})
from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
  d = {  'lst' : ['Seaum','Badhon','Abir'], 'birthday': datetime.datetime.now(), 'lstt': [1,2,3,34], 'seaum': 'seaum',}


  return render (request,'home.html',d)

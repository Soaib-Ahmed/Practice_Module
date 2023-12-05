from django.shortcuts import render,redirect
from .forms import ExampleForm,MyModelForm

def home(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MyModelForm()
    my_form = ExampleForm()
    return render(request, 'home.html', {'form': form})
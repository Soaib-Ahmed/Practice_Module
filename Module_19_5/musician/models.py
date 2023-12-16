from django.db import models

# @login_required(login_url='login')
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    instrument_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
# def add_musician(request):
#     if request.method == 'POST':
#         musician_form = MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician = musician_form.save(commit=False)
#             musician.user = request.user  # Associate the musician with the logged-in user
#             musician.save()
#             return redirect('add_musician')
#     else:
#         musician_form = MusicianForm()

#     return render(request, 'add_musician.html', {'form': musician_form})

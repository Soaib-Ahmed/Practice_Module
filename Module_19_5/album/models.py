from django.db import models
from musician.models import Musician

# Create your models here.
# class Album(models.Model):
#     try:
#         from musician.models import Musician
#     except ImportError:
#         pass

#     musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
#     album_name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

#     def __str__(self):
#         return self.album_name

from django.db import models
from django.conf import settings

# from django.db import models
# from django.conf import settings

# class Album(models.Model):
#     musician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='albums')
#     album_name = models.CharField(max_length=100)
#     release_date = models.DateField()
#     rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

#     def __str__(self):
#         return self.album_name

from django.db import models
from musician.models import Musician

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.album_name
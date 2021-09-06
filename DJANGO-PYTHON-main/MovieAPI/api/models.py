from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=200)
    genre=models.CharField(max_length=200)
    release_year=models.IntegerField()
    language=models.CharField(max_length=300)



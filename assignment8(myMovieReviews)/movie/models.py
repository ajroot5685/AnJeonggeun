from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    release_year = models.IntegerField()
    genre = models.TextField()
    star = models.FloatField()
    running_time = models.IntegerField()
    content = models.TextField()
    director = models.CharField(max_length=30)
    actor = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
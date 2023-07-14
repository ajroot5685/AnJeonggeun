from django.db import models

import random

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

    image=models.IntegerField(null=True)
    def save(self, *args, **kwargs):
        if not self.image:
            self.image=random.randint(0,7)
        super().save(*args, **kwargs)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
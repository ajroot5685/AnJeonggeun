from django.db import models

# Create your models here.
class Post(models.Model):
    # title, user, content, region, price
    title = models.CharField(max_length=64)
    user = models.CharField(max_length=32)
    content = models.TextField()
    region = models.CharField(max_length=16)
    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Like(models.Model):
    post_id = models.IntegerField()
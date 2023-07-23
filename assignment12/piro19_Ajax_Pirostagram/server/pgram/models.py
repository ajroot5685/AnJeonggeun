from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name=None
    last_name=None
    name = models.CharField(max_length=10, null=True, default="사용자")
    
    def __str__(self):
        return self.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    image = models.ImageField('이미지', blank=True, upload_to='idea/%Y%m%d')
    content = models.TextField()
    like = models.IntegerField(null=True, default=0)
    like_users = models.ManyToManyField(User, through='Like', related_name='liked_post')
    
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    text = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
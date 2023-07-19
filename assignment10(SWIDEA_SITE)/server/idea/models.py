from django.db import models

# Create your models here.
class Devtool(models.Model):
    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=40)
    content = models.TextField()

    def __str__(self):
        return self.name


class Idea(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField('이미지', blank=True, upload_to='idea/%Y%m%d')
    content = models.TextField()
    interest=models.IntegerField()
    devtool=models.ForeignKey(Devtool, verbose_name="개발 예상 툴", on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)
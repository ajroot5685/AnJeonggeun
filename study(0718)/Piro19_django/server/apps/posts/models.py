from django.db import models

class User(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField(default=0)

  def __str__(self):
    return self.name
  

class Post(models.Model):
  title = models.CharField('제목', max_length= 20)
  content = models.CharField('내용', max_length=20, blank=True)
  region = models.CharField('지역', max_length=20, blank=True)
  user = models.ForeignKey(User, verbose_name='작성자', on_delete=models.CASCADE)
  price = models.IntegerField('가격', default=1000)
  photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
  created_date = models.DateTimeField('작성일', blank=True, auto_created=True, auto_now_add=True)
  updated_date = models.DateTimeField('수정일', blank=True, auto_created=True, auto_now=True)
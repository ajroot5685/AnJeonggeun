from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    GENDER_CHOICE=[
        ('Male', '남자'),
        ('Female', '여자'),
    ]
    JOB_CHOICE=[
        ('Student','학생'),
        ('JobSeeker','취준생'),
        ('Worker','직장인'),
        ('Etc','기타'),
    ]
    first_name = None
    last_name = None
    name = models.CharField(max_length=10, null=True)
    email = models.EmailField(null=True)
    nickname = models.CharField(max_length=20, null=True)
    birth = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, null=True)
    job = models.CharField(max_length=10, choices=JOB_CHOICE, null=True)
    desc = models.TextField(max_length=100, blank=True, null=True)
from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    uid                 = models.BigAutoField(primary_key=True)
    username            = models.CharField(max_length=100, unique=True)
    password            = models.CharField(max_length=50)
    email               = models.EmailField(verbose_name="email", max_length=100, unique=True)
    phone_no            = models.CharField(max_length=12, null = True)
    pageviews           = models.BigIntegerField(default = 0)
    total_pages         = models.BigIntegerField(default = 0)
    upi                 = models.CharField(max_length=50, null = True)
    

    def __str__(self):
        return self.username
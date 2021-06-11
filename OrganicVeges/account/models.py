from django.db import models
from django.contrib.auth.models import User


class Mobile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=10)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)
    otp = models.CharField(max_length=6)

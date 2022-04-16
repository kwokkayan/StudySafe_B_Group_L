from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_device = models.BooleanField('Device Status', default=False)
    is_member = models.BooleanField('Member Status', default=False)

class DeviceAccounts (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__ (self):
        return str(self.user)

class MemberAccounts (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emailAddress = models.EmailField(verbose_name="email", max_length=60, unique=True)

    def __str__(self) :
        return str(self.user)

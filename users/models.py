from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class DeviceAccounts (AbstractUser):
    username = models.CharField(max_length=30, unique=True)

    def __str__ (self):
        return self.username

class MemberAccounts (AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emailAddress = models.EmailField(verbose_name="email", max_length=60, unique=True)

    def __str__(self) :
        return self.username

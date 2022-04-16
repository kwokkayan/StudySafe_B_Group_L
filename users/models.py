<<<<<<< Updated upstream
=======
from wsgiref.simple_server import demo_app
>>>>>>> Stashed changes
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
<<<<<<< Updated upstream
class DeviceAccounts (AbstractUser):
    username = models.CharField(max_length=30, unique=True)

=======

class User(AbstractUser):
    ROLES = (
        ('Device', 'Device'),
        ('Member', 'Member')
    )
    role_type = models.CharField(max_length=10, choices=ROLES, default=1)

class DeviceAccounts (models.Model):
    user = models.OneToOneField(User, related_name='device_account', on_delete=models.CASCADE, primary_key=True)
    def save(self, *args, **kwargs):
        if self.user.role_type == 'Member':
            return
        super().save(*args, **kwargs)
>>>>>>> Stashed changes
    def __str__ (self):
        return self.username

<<<<<<< Updated upstream
class MemberAccounts (AbstractUser):
    username = models.CharField(max_length=30, unique=True)
=======
class MemberAccounts (models.Model):
    user = models.OneToOneField(User, related_name='member_account', on_delete=models.CASCADE, primary_key=True)
>>>>>>> Stashed changes
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emailAddress = models.EmailField(verbose_name="email", max_length=60, unique=True)
    def save(self, *args, **kwargs):
        if self.user.role_type == 'Device':
            return
        super().save(*args, **kwargs)
    def __str__(self) :
        return self.username

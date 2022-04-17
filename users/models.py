from wsgiref.simple_server import demo_app
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES

# Create your models here.

class TaskforceAccount(AbstractUser):
    ROLES = (
        ('Device', 'Device'),
        ('Member', 'Member')
    )
    role_type = models.CharField(max_length=10, choices=ROLES, default=1)
    def clean (self):
        if self.role_type == 'Member' and (self.email in EMPTY_VALUES or self.first_name in EMPTY_VALUES or self.last_name in EMPTY_VALUES):
            raise ValidationError ({
                'email': ValidationError(("Missing email"), code='required'),
                'first_name': ValidationError(("Missing first_name"), code='required'),
                'last_name': ValidationError(("Missing last_name"), code='required')
            })

"""
class DeviceAccounts (models.Model):
    user = models.OneToOneField(User, related_name='device_account', on_delete=models.CASCADE, primary_key=True)
    def save(self, *args, **kwargs):
        if self.user.role_type == 'Member':
            return
        super().save(*args, **kwargs)
    def __str__ (self):
        return self.username

class MemberAccounts (models.Model):
    user = models.OneToOneField(User, related_name='member_account', on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    emailAddress = models.EmailField(verbose_name="email", max_length=60, unique=True)
    def save(self, *args, **kwargs):
        if self.user.role_type == 'Device':
            return
        super().save(*args, **kwargs)
    def __str__(self) :
        return self.username
"""

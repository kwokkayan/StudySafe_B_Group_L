from wsgiref.simple_server import demo_app
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES

# Create your models here.

class TaskforceAccount(AbstractUser):
    ROLES = (
        ('Device', 'Device'),
        ('Member', 'Member'),
        ('Admin', 'Admin')
    )
    role_type = models.CharField(max_length=10, choices=ROLES, default='Device')
    def clean (self):
        if self.role_type == 'Member' and (self.email in EMPTY_VALUES or self.first_name in EMPTY_VALUES or self.last_name in EMPTY_VALUES):
            raise ValidationError ({
                'email': ValidationError(("Missing email"), code='required'),
                'first_name': ValidationError(("Missing first_name"), code='required'),
                'last_name': ValidationError(("Missing last_name"), code='required')
            })
    def __str__(self):
        return "Username: {} User Type: {}".format(self.username, self.role_type)


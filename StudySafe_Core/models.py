from django.db import models
from django.forms import ValidationError

# Create your models here.
class HKUMember(models.Model):
    name = models.CharField(max_length=150)
    uid  = models.CharField(max_length=10, primary_key=True)
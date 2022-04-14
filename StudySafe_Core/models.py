#from django.contrib.auth.models import AbstractUser
from django.db import models

class Venues(models.Model):
        Venue_Code = models.CharField(max_length=20, unique=True,db_column='Venue Code')
        
        Location = models.CharField(max_length=150)

        ROOM_TYPE = (
                ('LT','LT'),
                ('CR','CR'),
                ('TR','TR')
        )
        Type = models.CharField(max_length=2, choices=ROOM_TYPE)

        Capacity = models.IntegerField()

        def __str__(self):
                return self.VenueCode


# Create your models here.

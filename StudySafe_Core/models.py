#from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError

# Create your models here.
class Venues(models.Model):
        Venue_Code = models.CharField(max_length=20, primary_key=True,db_column='Venue Code')
        
        Location = models.CharField(max_length=150)

        ROOM_TYPE = (
                ('LT','LT'),
                ('CR','CR'),
                ('TR','TR')
        )
        Type = models.CharField(max_length=2, choices=ROOM_TYPE)

        Capacity = models.IntegerField()

        def __str__(self):
            return self.Venue_Code

class HKUMember(models.Model):
    name = models.CharField(max_length=150)
    uid  = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return 'Name: {}, UID: {}'.format(self.uid, self.name)

class TravelRecord(models.Model):
    venue_code =  models.ForeignKey('Venues', on_delete=models.CASCADE)
    uid = models.ForeignKey('HKUMember', related_name='visited', on_delete=models.CASCADE)
    time_of_entry = models.DateTimeField()
    time_of_exit = models.DateTimeField(null=True)
    def __str__(self):
        return 'Travel Record ID: {}'.format(self.id)
from django.db import models
from django.forms import ValidationError

# Create your models here.
class HKUMember(models.Model):
    name = models.CharField(max_length=150)
    uid  = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return 'Name: {}, UID: {}'.format(self.name, self.uid)

class TravelRecord(models.Model):
    venue_code = models.CharField(max_length=20) #change to foreign key 
    uid = models.ForeignKey('HKUMember', related_name='visited', on_delete=models.CASCADE)
    time_of_entry = models.DateTimeField()
    time_of_exit = models.DateTimeField(null=True)
    def __str__(self):
        return 'Travel Record ID: {}'.format(self.id)
from django.db import models

# Create your models here.
class HKUMember(models.Model):
    name = models.CharField(max_length=150)
    uid  = models.CharField(max_length=10, primary_key=True)
    def __str__(self):
        return "NAME: {} UID: {}".format(self.name, self.uid)
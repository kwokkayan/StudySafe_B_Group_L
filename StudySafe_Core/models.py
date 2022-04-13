from django.db import models
from django.forms import ValidationError

# Create your models here.
class HKUMember(models.Model):
    name = models.CharField(max_length=150)
    uid  = models.CharField(max_length=10, primary_key=True)
    def check_save(self, success_message, *args, **kwargs):
        try: 
            super().full_clean()
            super().save(*args, **kwargs)
        except ValidationError as e:
            return e.__str__()
        return success_message
    def save(self, *args, **kwargs):
        if (self._state.adding):
            if (len(HKUMember.objects.all().filter(uid=self.uid)) > 0):
                return "Member already exists."
            else:
                return self.check_save("HKU Member registered.", *args, **kwargs)
        else:
            return self.check_save("HKU Member modified.", *args, **kwargs)
    def __str__(self):
        return "NAME: {} UID: {}".format(self.name, self.uid)
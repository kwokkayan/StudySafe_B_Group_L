from django.forms import ModelForm
from django.db import models
from .models import  TaskforceAccount
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES

#create user account

class CreateUser (UserCreationForm):
    
    class Meta:
        model = TaskforceAccount
        fields = ('username', 'role_type')

class ChangeUser (UserChangeForm):
    class Meta:
        model = TaskforceAccount
        fields = ('username', 'role_type')


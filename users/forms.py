from django.forms import ModelForm
from django.db import models
from .models import  TaskforceAccount
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import EMPTY_VALUES

#create user account

class CreateUser (UserCreationForm):
    
    class meta:
        model = TaskforceAccount
        fields = ('username', 'role_type')

class ChangeUser (UserChangeForm):
    class meta:
        model = TaskforceAccount
        fields = ('username', 'role_type')

"""
class DeviceCreation (ModelForm):
    class Meta:
        model = DeviceAccounts
        fields = ('__all__')

class MemberCreation (ModelForm):
    class Meta:
        model = MemberAccounts
        fields = ('__all__')

class DeviceChange (ModelForm):
    class Meta:
        model = DeviceAccounts
        fields = ('__all__')
        
class MemberChange (ModelForm):
    class Meta:
        model = MemberAccounts
        fields = ('__all__')
"""

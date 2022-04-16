from django.forms import ModelForm
from .models import DeviceAccounts, MemberAccounts
from django import forms

#create user account
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

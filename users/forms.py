from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from django import forms

#create user account
class DeviceCreation (UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class MemberCreation (UserCreationForm):
    first_name = forms.CharField (required=True)
    last_name = forms.CharField(required= True)
    emailAddress = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)

class DeviceChange (UserChangeForm):
    class Meta:
        model = User
        fields = ('username',)

class MemberChange (UserChangeForm):
    first_name = forms.CharField (required=True)
    last_name = forms.CharField(required= True)
    emailAddress = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username' ,'first_name', 'last_name', 'email',)

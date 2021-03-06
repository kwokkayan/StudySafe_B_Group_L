from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import DeviceAccounts, MemberAccounts

#create user account
class CreateMemberForm(UserCreationForm):
    class Meta:
        model = MemberAccounts
        fields = ('username', 'first_name', 'last_name', "emailAddress")
#create device account
class CreateDeviceForm(UserCreationForm):
    class Meta:
        model = DeviceAccounts
        fields = ('username',)
#change user account
class ChangeMemberForm(UserChangeForm):
    class Meta:
        model = MemberAccounts
        fields = ('username', 'first_name', 'last_name', "emailAddress")
#change device account
class ChangeDeviceForm(UserChangeForm):
    class Meta:
        model = DeviceAccounts
        fields = ('username', )
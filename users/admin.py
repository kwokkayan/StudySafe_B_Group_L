from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import DeviceCreation, DeviceChange, MemberCreation, MemberChange
from .models import User, DeviceAccounts, MemberAccounts
# Register your models here.



class DeviceAdmin (UserAdmin):
    add_form = DeviceCreation
    form = DeviceChange
    model = User
    list_display = ['username', ]

class MemberAdmin (UserAdmin):
    add_form = MemberCreation
    form = MemberChange
    model = User
    list_display = ['username', 'first_name', 'last_name', 'emailAddress',]


admin.site.register (DeviceAccounts )
admin.site.register (MemberAccounts)
admin.site.register (User)
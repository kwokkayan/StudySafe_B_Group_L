from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .users import ChangeDeviceForm, ChangeMemberForm, CreateDeviceForm, CreateMemberForm
from .models import DeviceAccounts, MemberAccounts

class DeviceAdmin (UserAdmin):
    add_form = CreateDeviceForm
    form = ChangeDeviceForm
    model = DeviceAccounts
    list_display = ['username', ]

class MemberAdmin (UserAdmin):
    add_form = CreateMemberForm
    form = ChangeDeviceForm
    model = MemberAccounts
    list_display = ['username', 'first_name', 'last_name', 'emailAddress',]


admin.site.register (DeviceAccounts, DeviceAdmin )
admin.site.register (MemberAccounts, MemberAdmin)
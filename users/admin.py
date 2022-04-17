from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

#from .users import ChangeDeviceForm, ChangeMemberForm, CreateDeviceForm, CreateMemberForm
from .models import  TaskforceAccount
from .forms import CreateUser, ChangeUser

class CustomUserAdmin (UserAdmin):
    form = ChangeUser
    add_from = CreateUser
    model = TaskforceAccount
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('role_type',)}),)
    list_filter = ["role_type"]

"""
class DeviceAdmin (UserAdmin):
    add_form = DeviceCreation
    form = DeviceChange
    model = DeviceAccounts
    list_display = ['username', ]

class MemberAdmin (UserAdmin):
    add_form = MemberCreation
    form = MemberChange
    model = MemberAccounts
    list_display = ['username', 'first_name', 'last_name', 'emailAddress',]


admin.site.register (DeviceAccounts)
admin.site.register (MemberAccounts)"""
#admin.site.register (User, CustomUserAdmin)
#admin.site.register(CheckUser)
admin.site.register (TaskforceAccount, CustomUserAdmin)

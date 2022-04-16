from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .users import ChangeDeviceForm, ChangeMemberForm, CreateDeviceForm, CreateMemberForm
from .models import DeviceAccounts, MemberAccounts

class DeviceAdmin (UserAdmin):
<<<<<<< Updated upstream
    add_form = CreateDeviceForm
    form = ChangeDeviceForm
=======
    add_form = DeviceCreation
    form = DeviceChange
>>>>>>> Stashed changes
    model = DeviceAccounts
    list_display = ['username', ]

class MemberAdmin (UserAdmin):
<<<<<<< Updated upstream
    add_form = CreateMemberForm
    form = ChangeDeviceForm
=======
    add_form = MemberCreation
    form = MemberChange
>>>>>>> Stashed changes
    model = MemberAccounts
    list_display = ['username', 'first_name', 'last_name', 'emailAddress',]


<<<<<<< Updated upstream
admin.site.register (DeviceAccounts, DeviceAdmin )
admin.site.register (MemberAccounts, MemberAdmin)
=======
admin.site.register (DeviceAccounts)
admin.site.register (MemberAccounts)
admin.site.register (User)
>>>>>>> Stashed changes

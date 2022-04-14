from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .users import ChangeDeviceForm, ChangeMemberForm, CreateDeviceForm, CreateMemberForm
from .models import deviceAccounts, MemberAccounts

#pls help help here, don't really understand
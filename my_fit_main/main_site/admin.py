from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *

UserAdmin.fieldsets += (('Custom fields',{'fields':('nickname','profile_pic','intro')}),)
admin.site.register(Food)
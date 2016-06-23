from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile
from .models import Product_Info

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'userprofile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )


# Register your models here.
admin.site.register(Product_Info)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
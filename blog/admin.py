# In your app's admin.py file

from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'full_name', 'gender', 'contact', 'address')
    search_fields = ('username', 'email', 'full_name')
    readonly_fields = ('id',)


admin.site.register(User, UserAdmin)

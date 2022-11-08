from django.contrib import admin
from website import models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'enabled')

admin.site.register(models.User, UserAdmin)
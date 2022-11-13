from django.contrib import admin
from website import models

# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'password', 'enabled')

class Member_infoAdmin(admin.ModelAdmin):
    list_display = ('room', 'bed', 'member_class', 'student_ID', 'name')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'about', 'country')

class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'user', 'title', 'content', 'created_at', 'updated_at')

# admin.site.register(models.User, UserAdmin)
admin.site.register(models.Member_info, Member_infoAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Post, PostAdmin)
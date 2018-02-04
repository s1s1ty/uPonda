# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Profile


def block_publisher(modeladmin, request, queryset):
    for member in queryset:
        member.active = 0
        member.save()


class UserAdmin(admin.ModelAdmin):
    actions = [block_publisher]
    list_display = ['username', 'email', 'is_active', 'is_staff']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_type']


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

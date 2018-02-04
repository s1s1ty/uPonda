# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Book


def approve_published_book(modeladmin, request, queryset):
    for book in queryset:
        book.approve = 1
        book.publication_status = 1
        book.save()


def cancel_published_book(modeladmin, request, queryset):
    for book in queryset:
        book.publication_status = 0
        book.approve = 0 # because want to filter books only this field
        book.save()


class BookAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'ISBN_No', 'approve', 'publication_status']
    actions = [approve_published_book, cancel_published_book]


admin.site.register(Book, BookAdmin)
admin.site.disable_action('delete_selected')

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from core.models import Book

class Profile(models.Model):
    USER_CHOICES = (
        ('P', 'Publisher'),
        ('M', 'Member')
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    user_type = models.CharField(max_length=1, choices=USER_CHOICES)
    subscribe_books = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return self.user_type

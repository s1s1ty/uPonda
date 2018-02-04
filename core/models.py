# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ISBN_No = models.CharField(max_length=500)
    cover_photo = models.ImageField(upload_to='cover_photo')
    pdf = models.FileField(upload_to='pdf')
    approve = models.BooleanField(default=False)
    publication_status = models.BooleanField(default=True)

    subscribers = models.ManyToManyField(User, blank=True, related_name='book_subscribers')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/book/detail/%i/" % self.id

    def get_subscribe_url(self):
        return "/book/detail/%i/subscribe/" % self.id


# class BookFeedback(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     rate = models.IntegerField(default=0)
#     review = models.TextField()

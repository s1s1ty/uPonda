# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField()
    rating = models.PositiveIntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    @property
    def rating_text(self):
    	if self.rating == 1:
    		return 'Good'
    	elif self.rating == 2:
    		return 'Average'
    	elif self.rating == 3:
    		return 'Bad'
    	else:
    		return 'No Feedback'

from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User


class Book(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	cover_pic = models.ImageField()
	created_date = models.DateField(default=datetime.datetime.now())
	tag = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('book_name_update', kwargs={'pk': self.pk})


class BookDetails(models.Model):
	book_name = models.ForeignKey(Book, on_delete = models.CASCADE)
	chapter_name = models.CharField(max_length=300, blank=False, null=False)
	chapter_details = models.TextField()

	def __str__(self):
		return self.chapter_name

	def get_absolute_url(self):
		return reverse('update_detail', kwargs={'pk': self.pk})

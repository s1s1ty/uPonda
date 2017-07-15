from django import forms
from .models import Book, BookDetails

from pagedown.widgets import PagedownWidget

class BookWriteForm(forms.ModelForm):
	name = forms.CharField(label='', widget=forms.TextInput(attrs={
	'class': 'form-control',
	'placeholder': 'Book Name'
	}))
	tag = forms.CharField(label='', widget=forms.TextInput(attrs={
	'class': 'form-control',
	'placeholder': 'Book type(Use comma if multiple tags)'
	}))
	cover_pic = forms.ImageField(label='', widget=forms.FileInput(attrs={
	'class': 'form-control'
	}))
	class Meta:
		model  = Book
		fields = ['name', 'tag', 'cover_pic']


class BookWriteDetailForm(forms.ModelForm):
	chapter_details = forms.CharField(widget=PagedownWidget)
	chapter_name = forms.CharField(widget=forms.TextInput(attrs={
	'class': 'form-control',
	'placeholder': 'Chapter Name'
	}))
	class Meta:
		model = BookDetails
		fields = ['book_name', 'chapter_name', 'chapter_details']

	# def __init__(self, request, *args,**kwargs):
	# 	super (BookWriteDetailForm,self ).__init__(*args,**kwargs)
	# 	self.fields['book_name'].queryset = Book.objects.filter(author=request.user)
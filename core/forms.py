from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Book Name'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Description'
    }))
    ISBN_No = forms.CharField(label='ISBN NO', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ISBN NO'
    }))
    cover_photo = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    pdf = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = Book
        exclude = ('approve', 'publication_status', 'user', 'subscribers')
        fields = '__all__'

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.db.models import Q

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from . models import Book, BookDetails
from . forms import BookWriteForm, BookWriteDetailForm


class AllBookIndex(generic.ListView):
	template_name = 'books/index.html'
	model = Book
	def get_queryset(self):
		queryset = super(AllBookIndex, self).get_queryset()
		query = self.request.GET.get('q')
		if query:
			queryset = queryset.filter(Q(name__icontains=query)|
								  Q(tag__icontains=query))
		return queryset

class MyBookIndex(generic.ListView):
	template_name = 'books/index.html'
	model = Book

	def get_queryset(self):
		queryset = super(MyBookIndex, self).get_queryset()
		queryset = queryset.filter(author=self.request.user)
		query = self.request.GET.get('q')
		if query:
			queryset = queryset.filter(Q(name__icontains=query)|
								  Q(tag__icontains=query)|
								  Q(author__icontains=query))
		return queryset
		
class BookDetailView(generic.DeleteView):
	model = Book
	template_name = 'books/book_detail.html'
		
class BookWriteView(generic.View):
	"""docstring for BookWrite"""
	template_name = 'books/book_form.html'
	model = Book
	form_class = BookWriteForm
	success_url = reverse_lazy('my_booklist')

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST, request.FILES)
		if form.is_valid():
			obj = form.save(commit=False)
			user = User.objects.get(id=request.user.id)
			obj.author = user
			obj.save()
			return redirect('/book/mybook/')
		return render(request, self.template_name, {'form': form})

class BookUpdateView(UpdateView):
	template_name = 'books/book_form.html'
	model = Book
	form_class = BookWriteForm
	success_url = reverse_lazy('booklist')


class ChapterCreateView(CreateView):
	template_name = 'books/book_form.html'
	model = BookDetails
	success_url = reverse_lazy('booklist')
	form_class = BookWriteDetailForm
	
	# def get(self, request):
		# for filter book name by login user
		# form_class = BookWriteDetailForm 
		# return render(request, self.template_name, {'form': form_class})


class ChapterUpdateView(UpdateView):
	template_name = 'books/book_form.html'
	model = BookDetails
	form_class = BookWriteDetailForm
	success_url = reverse_lazy('chapter_list')


class ChapterListView(generic.ListView):
	template_name = 'books/book_detail.html'
	model = BookDetails

class ChapterDetailView(generic.DetailView):
	template_name = 'books/show_detail.html'
	model = BookDetails

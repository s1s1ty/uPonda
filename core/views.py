# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.views import generic
from django.db.models import Q

from .models import Book
from comment.models import Comment
from .forms import BookForm
from comment.forms import CommentForm


class IndexView(generic.ListView):
    template_name = 'cores/index.html'
    model = Book

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        queryset = queryset.filter(approve=1)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        return queryset


class CreateBookView(generic.View):
    template_name = 'cores/book_form.html'
    model = Book
    form_class = BookForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            user = self.request.user
            obj.user = user
            obj.save()
            messages.success(request, 'Successfully Created & Send For Admin Review')
            return redirect('/my-books/')
        return render(request, self.template_name, {'form': form})


class BookDetailView(generic.View):
    template_name = 'cores/book_detail.html'
    model = Book
    form_class = CommentForm

    # def comment_data(self, **kwargs):
    #     content_type = ContentType.objects.get_for_model(self.model)
    #     obj_id = kwargs.get('object').id
    #     comments = Comment.objects.filter(content_type=content_type, object_id=obj_id)
    #     return comments
    #
    # def get_context_data(self, **kwargs):
    #     context = super(BookDetailView, self).get_context_data(**kwargs)
    #     comments = self.comment_data(**kwargs)
    #     extra_context = {
    #         'comments': comments
    #     }
    #     context.update(extra_context)
    #     return context
    #
    def get(self, request, pk, *args, **kwargs):
        form = self.form_class(None)
        instance = self.model.objects.get(pk=pk)
        content_type = ContentType.objects.get_for_model(self.model)
        obj_id = instance.id
        comments = Comment.objects.filter(content_type=content_type, object_id=obj_id)
        # average_rating = comments.objects.aggregate(Avg('rating'))

        context = {
            'object': instance,
            'comments': comments,
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        instance = self.model.objects.get(pk=pk)
        if form.is_valid():
            obj = form.save(commit=False)
            user = self.request.user
            obj.content_type = ContentType.objects.get_for_model(self.model)
            obj.object_id = instance.id
            obj.user = user
            obj.rating = request.POST.get('rating')
            obj.save()
            content_type = ContentType.objects.get_for_model(self.model)
            comments = Comment.objects.filter(content_type=content_type, object_id=instance.id)
            form = self.form_class(None)

        context = {
            'object': instance,
            'comments': comments,
            'form': form
        }
        return render(request, self.template_name, context)


class MyBookView(generic.ListView):
    template_name = 'cores/index.html'
    model = Book

    def get_queryset(self):
        queryset = super(MyBookView, self).get_queryset()
        queryset = queryset.filter(user=self.request.user).filter(approve=1)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query))
        return queryset


class BookSubscribeToggle(generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        pk = kwargs.get('pk')
        obj = get_object_or_404(Book, pk=pk)
        user = self.request.user
        total_subscribed_book = user.profile.subscribe_books.count()
        if user.is_authenticated():
            if user in obj.subscribers.all():
                obj.subscribers.remove(user)  
                user.profile.subscribe_books.remove(obj)
            else:
                if total_subscribed_book < 3:
                    obj.subscribers.add(user)
                    user.profile.subscribe_books.add(obj)
                else:
                    messages.error(self.request, 'Sorry you have already subscribe 3 books!')
        return obj.get_absolute_url()
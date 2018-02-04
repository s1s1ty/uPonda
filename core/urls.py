from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^my-books/$', views.MyBookView.as_view(), name='my_books'),
    url(r'^my-book/add/$', views.CreateBookView.as_view(), name='add_book'),
    url(r'^book/detail/(?P<pk>\d+)/$', login_required(views.BookDetailView.as_view()), name='detail_book'),
    url(r'^book/detail/(?P<pk>\d+)/subscribe/$', views.BookSubscribeToggle.as_view(), name='subscribe'),
]

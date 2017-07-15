from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$',views.AllBookIndex.as_view(), name='booklist'),
    url(r'^mybook/$',views.MyBookIndex.as_view(), name='my_booklist'),

    url(r'^write/$',login_required(views.BookWriteView.as_view()), name='bookname'),
    url(r'^update/(?P<pk>[0-9]+)/$',views.BookUpdateView.as_view(), name='book_name_update'),
    url(r'^read/(?P<pk>\d+)/$',login_required(views.BookDetailView.as_view()), name='read_book'),

   	url(r'^write_detail/$',views.ChapterCreateView.as_view(), name='chapter_write'),
   	url(r'^update_detail/(?P<pk>[0-9]+)/$',views.ChapterUpdateView.as_view(), name='chapter_update'),
]

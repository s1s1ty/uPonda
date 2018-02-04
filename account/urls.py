from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # user authentication urls
    url(r'^join/$', views.UserJoinView.as_view(), name='join'),
    url(r'^login/$', views.UserLoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]

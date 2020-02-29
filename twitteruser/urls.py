from django.contrib import admin
from django.urls import path, include

from twitteruser import views

urlpatterns = [
path("twitteruser/<str:twitteruser>", views.twitteruser, name='twitteruser'),
path("follow/<str:twitteruser>", views.follow_add_view, name="follow"),
path("unfollow/<str:twitteruser>", views.follow_remove_view, name="unfollow"),
path("follows/<str:twitteruser>", views.follow_view, name="follows")
]
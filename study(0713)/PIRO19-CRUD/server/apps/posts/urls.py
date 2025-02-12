from django.urls import path

from server.apps.posts.views import *

urlpatterns = [
    path('', posts_list),
    path('posts/<int:pk>', posts_read),
    path('posts/create', posts_create),
    path('posts/like', posts_like),
    path('posts/<int:pk>/delete', posts_delete),
    path('posts/<int:pk>/update', posts_update),
]

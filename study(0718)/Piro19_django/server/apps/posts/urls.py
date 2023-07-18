from django.urls import path
from apps.posts import views

app_name="posts"

urlpatterns = [    
    path('', views.main),
    path('posts/detail/<int:pk>', views.detail, name='detail'),
    path('posts/create', views.create, name='create'),
    path('posts/update/<int:pk>', views.update, name='update'),
    path('posts/delete/<int:pk>', views.delete, name='delete'),
]
from django.urls import path
from idea import views

app_name="idea"

urlpatterns = [    
    path('', views.idea_list),
    # path('posts/detail/<int:pk>', views.detail, name='detail'),
    # path('posts/create', views.create, name='create'),
    # path('posts/update/<int:pk>', views.update, name='update'),
    # path('posts/delete/<int:pk>', views.delete, name='delete'),
]
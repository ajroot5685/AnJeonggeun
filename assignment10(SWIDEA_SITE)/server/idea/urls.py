from django.urls import path
from idea import views

app_name="idea"

urlpatterns = [    
    # path('', views.idea_list, name='list'),
    path('', views.idea_devdetail, name='list'),
    path('ideas/create', views.idea_create, name='create'),
    # path('ideas/detail/<int:pk>', views.idea_detail, name='detail'),
    # path('ideas/devtool/list', views.idea_devlist, name='devlist'),
    # path('ideas/devtool/register', views.idea_devregister, name='devregister'),
    # path('ideas/devtool/detail/<int:pk>', views.idea_devdetail, name='idea_devdetail'),
    
]
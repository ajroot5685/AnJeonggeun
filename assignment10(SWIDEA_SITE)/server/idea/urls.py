from django.urls import path
from idea import views

app_name="idea"

urlpatterns = [    
    path('', views.idea_list, name='list'),
    path('ideas/create', views.idea_create, name='create'),
    path('ideas/<int:pk>', views.idea_detail, name='detail'),
    path('ideas/<int:pk>/delete', views.idea_delete, name='delete'),
    path('ideas/<int:pk>/update', views.idea_update, name='update'),
    path('ideas/devtool/list', views.idea_devlist, name='devlist'),
    path('ideas/devtool/register', views.idea_devregister, name='devregister'),
    path('ideas/devtool/<int:pk>', views.idea_devdetail, name='idea_devdetail'),
    path('ideas/devtool/<int:pk>/delete', views.idea_devdelete, name='idea_devdelete'),
    path('ideas/devtool/<int:pk>/update', views.idea_devupdate, name='idea_devupdate'),
    
]
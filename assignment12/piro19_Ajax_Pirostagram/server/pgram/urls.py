from django.urls import path
from pgram import views

app_name="pgram"

urlpatterns = [    
    path('', views.pgram_list, name='list'),
    path('pgram/create', views.pgram_create, name='create'),
    path("pgram/login", views.pgram_login, name="login"),
    path("pgram/logout", views.pgram_logout, name="logout"),
    path("pgram/signup", views.pgram_signup, name="signup"),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
]
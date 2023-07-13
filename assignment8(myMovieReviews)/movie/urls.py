from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('', movies_list),
    path('movies/<int:pk>', movies_read),
    path('movies/create', movies_create),
    path('movies/<int:pk>/delete', movies_delete),
    path('movies/<int:pk>/update', movies_update),
]

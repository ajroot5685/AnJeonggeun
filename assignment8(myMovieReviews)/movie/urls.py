from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('', movies_list),
    path('movies/create', movies_create),
]

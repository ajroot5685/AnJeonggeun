from django.urls import path
from movie.views import *

app_name = 'movie'

urlpatterns = [
    path('tmp', movies_list),
    path('', movies_create),
]

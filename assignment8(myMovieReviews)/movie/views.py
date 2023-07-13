from django.shortcuts import render

# Create your views here.
def movies_list(request):
    return render(request, "movie/movies_list.html")

def movies_create(request):
    return render(request, "movie/movies_create.html")
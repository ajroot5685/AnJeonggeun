from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def movies_list(request, *args, **kwargs):
    movies=Movie.objects.all()
    return render(request, "movie/movies_list.html", {"movies": movies})

def movies_read(request, pk, *args, **kwargs):
    movies = Movie.objects.get(id=pk)

    return render(request, "movie/movies_read.html", {"movies":movies})

def movies_create(request, *args, **kwargs):
    if request.method == "POST":
        Movie.objects.create(
            title=request.POST["title"],
            release_year=request.POST["release_year"],
            genre=request.POST["genre"],
            star=request.POST["star"],
            running_time=request.POST["running_time"],
            content=request.POST["content"],
            director=request.POST["director"],
            actor=request.POST["actor"],
        )
        return redirect("/")
    return render(request, "movie/movies_create.html")
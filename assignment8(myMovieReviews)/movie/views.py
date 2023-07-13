from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def movies_list(request, *args, **kwargs):
    movies=Movie.objects.all()
    return render(request, "movie/movies_list.html", {"movies": movies})

def movies_read(request, pk, *args, **kwargs):
    movie = Movie.objects.get(id=pk)

    print(movie.id)

    if request.method == "POST":
        return redirect(f"/movies/{movie.id}")

    return render(request, "movie/movies_read.html", {"movie":movie})

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

def movies_delete(request, pk, *args, **kwargs):
    movie=Movie.objects.get(id=pk)
    movie.delete()
    return redirect("/")

def movies_update(request, pk, *args, **kwargs):

    movie = Movie.objects.get(id=pk)

    if request.method == "POST":
        movie.title=request.POST["title"]
        movie.release_year=request.POST["release_year"]
        movie.genre=request.POST["genre"]
        movie.star=request.POST["star"]
        movie.running_time=request.POST["running_time"]
        movie.content=request.POST["content"]
        movie.director=request.POST["director"]
        movie.actor=request.POST["actor"]
        movie.save()
        return redirect(f"/movies/{movie.id}")

    return render(request, "movie/movies_update.html", {"movie":movie})
from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def movies_list(request, *args, **kwargs):
    sort=""

    if request.method == "POST":
        movie_order=request.POST["order"]
        order_direction=request.POST["direction"]
        if order_direction=="내림차순":
            sort="-"
        if movie_order=="영화제목 순":
            sort+="title"
        elif movie_order=="개봉년도 순":
            sort+="release_year"
        elif movie_order=="별점 순":
            sort+="star"
        elif movie_order=="러닝타임 순":
            sort+="running_time"

    if sort!="":
        movies=Movie.objects.all().order_by(sort)
    else:
        movies=Movie.objects.all()

    return render(request, "movie/movies_list.html", {"movies": movies})

def movies_read(request, pk, *args, **kwargs):
    movie = Movie.objects.get(id=pk)

    movie_rt = movie.running_time
    hour=str(movie_rt//60)
    minutes=str(movie_rt%60)
    movie_rt=hour+'시간 '+minutes+'분'

    return render(request, "movie/movies_read.html", {"movie":movie, "movie_rt":movie_rt})

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
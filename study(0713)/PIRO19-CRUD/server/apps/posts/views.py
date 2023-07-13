from django.shortcuts import render, redirect
from .models import Post, Like

from django.http.request import HttpRequest
from django.db.models import Q

# Create your views here.
def hello_world(request):
    return render(request, "posts/hello_world.html")

def posts_list(request: HttpRequest, *args, **kwargs):

    # 값이 없을 경우에 오류가 발생함
    # text = request.GET["text"]
    
    # 값이 없을 경우 None을 반환한다.
    text = request.GET.get("text")
    min = request.GET.get("min_price")
    max = request.GET.get("max_price")

    posts=Post.objects.all()
    
    if text:
        # 장고 쿼리셋 lookup
        # __contains(언더바 2개) 를 붙여서 포함여부를 필터링할 수 있다.
        # posts = posts.filter(title__contains=text)

        # from django.db.models import Q 를 포함해야한다.
        # or만 Q가 필수이고, and는 그냥 쉼표로 연결해도 된다.
        posts = posts.filter(Q(title__contains=text) | Q(content__contains=text))

    if min and max and min <= max:
        posts = posts.filter(price__gte=min, price__lte=max)
    elif min:
        posts = posts.filter(price__gte=min)
    elif max:
        posts = posts.filter(price__lte=max)

    return render(request, "posts/posts_list.html", {"posts":posts})

def posts_read(request, pk, *args, **kwargs):
    # # 튜플
    # print(args)
    # # 딕셔너리
    # print(kwargs)

    # post = Post.objects.get(id=kwargs['pk'])
    # 위 코드를 사용하려면 kwargs에 인자가 들어가도록 pk 파라미터를 삭제해야함
    post = Post.objects.get(id=pk)

    # 현재 글에 이미 좋아요를 눌렀는지 검사
    # 이미 눌렀으면 like에 뭐가 들어있음.
    # get을 안쓰고 filter를 쓴 이유 : get은 아무것도 없으면 오류가 나기 때문
    like = Like.objects.filter(post_id=pk).first()

    if request.method == "POST":
        if like==None:
            Like.objects.create(post_id=pk)
        else:
            like.delete()
        return redirect(f"/posts/{post.id}")

    return render(request, "posts/posts_read.html", {"post":post, "like":like})

# create
def posts_create(request, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
                title=request.POST["title"],
                user=request.POST["user"],
                region=request.POST["region"],
                price=request.POST["price"],
                content=request.POST["content"],
            )
        return redirect("/")
    return render(request, "posts/posts_create.html")

def posts_delete(request, pk, *args, **kwargs):
    # DELETE / PUT... -> REST API
    # 삭제해야 할 때 -> 삭제하기 버튼 눌러서 POST로 왔을 때
    if request.method=="POST":
        post=Post.objects.get(id=pk)
        post.delete()
        like = Like.objects.filter(post_id=pk).first()
        if like!=None:
            like.delete()


    return redirect("/")

def posts_update(request, pk, *args, **kwargs):

    post = Post.objects.get(id=pk)

    if request.method == "POST":
        # 수정하는 부분
        post.title=request.POST["title"]
        post.user=request.POST["user"]
        post.region=request.POST["region"]
        post.price=request.POST["price"]
        post.content=request.POST["content"]
        post.save()
        return redirect(f"/posts/{post.id}")

    return render(request, "posts/posts_update.html", {"post":post})

# 좋아요 목록 페이지
def posts_like(request, *args, **kwargs):

    likes = Like.objects.all()

    posts=[]
    for like in likes:
        posts.append(Post.objects.get(id=like.post_id))

    return render(request, "posts/posts_like.html", {"posts":posts})
from django.shortcuts import render, redirect
from .models import Idea, Devtool

def idea_list(request):
    sort=""

    if request.method == "POST":
        idea_order=request.POST["order"]
        if idea_order=="찜하기순":
            sort=""
            # 수정 필요
        elif idea_order=="등록순":
            sort="created_at"
        elif idea_order=="최신순":
            sort="-updated_at"
        elif idea_order=="이름순":
            sort="title"

    if sort!="":
        ideas=Idea.objects.all().order_by(sort)
    else:
        ideas=Idea.objects.all()

    ctx = {
        'ideas': ideas,
    }
    return render(request, 'idea/idea_list.html', context=ctx)

def idea_create(request):

    if request.method == "POST":
        if request.FILES.get('image'):
            tmpimage=request.FILES['image']
            Idea.objects.create(
                title=request.POST["title"],
                image=tmpimage,
                content=request.POST["content"],
                interest=request.POST["interest"],
                devtool=Devtool.objects.get(name=request.POST["devtool"]),
            )
        else:
            Idea.objects.create(
                title=request.POST["title"],
                content=request.POST["content"],
                interest=request.POST["interest"],
                devtool=Devtool.objects.get(name=request.POST["devtool"]),
            )

        return redirect("/")
    
#     if request.method == 'GET':
    #     form = PostForm()
    #     ctx = {'form': form}
    #     return render(request, 'posts/post_create.html', context = ctx)    
    #   else:
    #     form = PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #       form.save()      
    #     return redirect('/')

    devtools = Devtool.objects.all()

    ctx={
        'devtools': devtools,
    }

    return render(request, 'idea/idea_create.html', context=ctx)

def idea_detail(request, pk):
    idea = Idea.objects.get(id=pk)

    devtool = idea.devtool

    ctx={
        'idea': idea,
        'devtool' : devtool,
    }

    return render(request, 'idea/idea_detail.html', context=ctx)

def idea_devlist(request):

    devtools = Devtool.objects.all()

    ctx = {
        'devtools': devtools,
    }

    return render(request, 'idea/idea_devlist.html', context=ctx)

def idea_devregister(request):

    if request.method == "POST":
        Devtool.objects.create(
            name=request.POST["name"],
            kind=request.POST["kind"],
            content=request.POST["content"],
        )
        return redirect("/")

    return render(request, 'idea/idea_devregister.html')

def idea_devdetail(request, pk):

    devtool = Devtool.objects.get(id=pk)

    related_ideas=devtool.idea_set.all()

    ctx={
        'devtool': devtool,
        'related_ideas' : related_ideas,
    }

    return render(request, 'idea/idea_devdetail.html', context=ctx)
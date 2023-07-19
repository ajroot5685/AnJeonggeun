from django.shortcuts import render, redirect, HttpResponse
from .models import Idea, Devtool, IdeaStar

from django.http import JsonResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest'

def idea_list(request):
    if is_ajax(request=request):
        if request.POST.get("function")=="interest":
            idea_id=request.POST.get("idea_id")
            action = request.POST.get("action")

            idea_ajax=Idea.objects.get(pk=idea_id)
            if action=="increase" and idea_ajax.interest<10:
                idea_ajax.interest+=1
            elif action=="decrease" and idea_ajax.interest>0:
                idea_ajax.interest-=1
            idea_ajax.save()
            response_data = {"new_interest":idea_ajax.interest}
            return JsonResponse(response_data)
        elif request.POST.get("function")=="star":
            idea_id=request.POST.get("idea_id")
            idea_ajax=Idea.objects.get(pk=idea_id)

            ideastar=IdeaStar.objects.filter(idea=idea_ajax)
            isStar=ideastar.exists()

            if isStar:
                ideastar.delete()
                response_data = {"star":"☆"}
            else:
                IdeaStar.objects.create(
                    idea=idea_ajax
                )
                response_data = {"star":"★"}
            return JsonResponse(response_data)


    sort=""
    ideastars=IdeaStar.objects.all()

    if request.method == "POST":
        idea_order=request.POST["order"]
        if idea_order=="찜하기순":
            ideas_isstar=Idea.objects.filter(ideastar__isnull=False)
            ideas_isnotstar=Idea.objects.filter(ideastar__isnull=True)
            sort="!"
        elif idea_order=="등록순":
            sort="created_at"
        elif idea_order=="최신순":
            sort="-updated_at"
        elif idea_order=="이름순":
            sort="title"

    if sort=="!":
        ideas=list(ideas_isstar)+list(ideas_isnotstar)
    elif sort!="":
        ideas=Idea.objects.all().order_by(sort)
    else:
        ideas=Idea.objects.all()

    page=request.GET.get('page')
    paginator = Paginator(ideas, 4)
    try:
        page_obj=paginator.page(page)
    except PageNotAnInteger:
        page_obj=paginator.page(1)
    except EmptyPage:
        page_obj=paginator.page(1)

    ctx = {
        'ideas': ideas,
        'ideastars': ideastars,
        'page_obj': page_obj,
        'paginator': paginator,
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
    
    devtools = Devtool.objects.all()

    ctx={
        'devtools': devtools,
    }

    return render(request, 'idea/idea_create.html', context=ctx)

def idea_detail(request, pk):
    if is_ajax(request=request):
        idea_id=request.POST.get("idea_id")
        idea_ajax=Idea.objects.get(pk=idea_id)

        ideastar=IdeaStar.objects.filter(idea=idea_ajax)
        isStar=ideastar.exists()

        if isStar:
            ideastar.delete()
            response_data = {"star":"☆"}
        else:
            IdeaStar.objects.create(
                idea=idea_ajax
            )
            response_data = {"star":"★"}
        return JsonResponse(response_data)

    idea = Idea.objects.get(id=pk)

    devtool = idea.devtool

    ideastars = IdeaStar.objects.all()

    ctx={
        'idea': idea,
        'devtool' : devtool,
        'ideastars' : ideastars,
    }

    return render(request, 'idea/idea_detail.html', context=ctx)

def idea_delete(request, pk):
    idea = Idea.objects.get(id=pk)

    idea.delete()

    return redirect("/")

def idea_update(request, pk):
    
    idea = Idea.objects.get(id=pk)

    if request.method == "POST":
        idea.title=request.POST["title"]
        idea.content=request.POST["content"]
        idea.interest=request.POST["interest"]
        idea.devtool=Devtool.objects.get(name=request.POST["devtool"])

        if request.FILES.get('image'):
            tmpimage=request.FILES['image']
            idea.image=tmpimage
            
        elif request.POST.get('clear') != None:
            idea.image=None
        idea.save()
            
        return redirect(f"/ideas/{idea.pk}")
    
    devtools = Devtool.objects.all()

    ctx={
        'idea':idea,
        'devtools': devtools,
    }

    return render(request, "idea/idea_update.html", context=ctx)

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
        return redirect("/ideas/devtool/list")

    return render(request, 'idea/idea_devregister.html')

def idea_devdetail(request, pk):

    devtool = Devtool.objects.get(id=pk)

    related_ideas=devtool.idea_set.all()

    ctx={
        'devtool': devtool,
        'related_ideas' : related_ideas,
    }

    return render(request, 'idea/idea_devdetail.html', context=ctx)

def idea_devdelete(request, pk):

    devtool = Devtool.objects.get(id=pk)

    devtool.delete()

    return redirect("/")

def idea_devupdate(request, pk):
    
    devtool = Devtool.objects.get(id=pk)


    if request.method == "POST":
        devtool.name=request.POST["name"]
        devtool.kind=request.POST["kind"]
        devtool.content=request.POST["content"]
        devtool.save()
            
        return redirect(f"/ideas/devtool/{devtool.pk}")

    ctx={
        'devtool':devtool,
    }

    return render(request, "idea/idea_devupdate.html", context=ctx)
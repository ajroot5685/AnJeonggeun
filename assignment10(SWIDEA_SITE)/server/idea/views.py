from django.shortcuts import render, redirect
# from .models import Idea

def idea_list(request):
    # ideas = Idea.objects.all()

    # ctx = {
    #     'ideas': ideas,
    # }
    return render(request, 'idea/idea_list.html')

def idea_create(request):

    return render(request, 'idea/idea_create.html')

def idea_detail(request):

    return render(request, 'idea/idea_detail.html')

def idea_devlist(request):

    return render(request, 'idea/idea_devlist.html')

def idea_devregister(request):

    return render(request, 'idea/idea_devregister.html')

def idea_devdetail(request):

    return render(request, 'idea/idea_devdetail.html')
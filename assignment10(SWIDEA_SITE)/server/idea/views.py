from django.shortcuts import render, redirect
# from .models import Idea

def idea_list(request):
    # ideas = Idea.objects.all()

    # ctx = {
    #     'ideas': ideas,
    # }
    return render(request, 'idea/idea_list.html')
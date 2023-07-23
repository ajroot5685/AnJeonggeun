from django.shortcuts import render, redirect
from .models import User,Post,Comment, Like

from pgram.forms import SignupForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def pgram_list(request):
    
    posts=Post.objects.all()
    likes=Like.objects.all()

    if request.user.is_authenticated:
        current_user = request.user
    else:
        current_user=None

    ctx={
        'posts':posts,
        'user':current_user,
        'likes':likes,
    }

    return render(request, 'pgram/pgram_list.html', context=ctx)

def pgram_create(request):

    users=User.objects.all()

    if request.user.is_authenticated:
        if request.user.is_superuser:
            auth.logout(request)
            return redirect('/')
        current_user = request.user

    if request.method == "POST":
        if request.FILES.get('image'):
            tmpimage=request.FILES['image']
            post=Post.objects.create(
                user=current_user,
                image=tmpimage,
                content=request.POST["content"],
            )
        else:
            post=Post.objects.create(
                user=current_user,
                content=request.POST["content"],
            )
        post_pk=str(post.pk)
        return redirect("/")

    ctx={
    }

    return render(request, 'pgram/pgram_create.html', context=ctx)

def pgram_signup(request):

    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('/')
        else:
            ctx={
                'form':form,
            }
            return render(request, 'pgram/pgram_signup.html',context=ctx)
    else:
        form = SignupForm()
        ctx={
            'form':form,
        }
        return render(request, 'pgram/pgram_signup.html',context=ctx)

def pgram_login(request):
    if request.method=='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('/')
        else:
            ctx={
                'form':form,
            }
            return render(request, template_name='pgram/pgram_login.html', context=ctx)
    else:
        form = AuthenticationForm()
        ctx={
            'form':form,
        }
        return render(request, template_name='pgram/pgram_login.html', context=ctx)

def pgram_logout(request):
    auth.logout(request)
    return redirect('/')

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    user_id = req['userid']
    button_type = req['type']

    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=user_id)

    if button_type=='like':
        post.like+=1
        Like.objects.create(
            post = post,
            user = user,
        )
    else:
        post.like-=1
        Like.objects.filter(user=user,post=post).delete()

    post.save()

    return JsonResponse({'id':post_id, 'userid':user_id, 'type':button_type})
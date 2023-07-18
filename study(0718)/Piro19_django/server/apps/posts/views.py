from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def main(request):
  try:
    # search_txt = request.GET.get('search_txt')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    posts = Post.objects.all().filter(price__gt=min_price, price__lt=max_price)
  except:
    posts = Post.objects.all()

  ctx = {
    'posts': posts,
  }
  return render(request, 'posts/post_list.html', context=ctx)


def create(request):
  if request.method == 'GET':
    form = PostForm()
    ctx = {'form': form}
    return render(request, 'posts/post_create.html', context = ctx)    
  else:
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()      
    return redirect('/')
  

def detail(request, pk):
  target_post = Post.objects.get(id = pk)
  ctx = {'post' : target_post,}
  return render(request, 'posts/post_detail.html', context=ctx)
  
  
def update(request, pk):
  if request.method == 'GET':
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)    
    ctx = {'form': form,
           'pk': pk}  
    
    return render(request, 'posts/post_update.html', context=ctx)
  else:
    post = Post.objects.get(id=pk)
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():      
      form.save()
    return redirect(f'/posts/detail/{pk}', pk)
  
  
def delete(request, pk):
  post = Post.objects.get(id=pk)
  post.delete()
  return redirect('/')
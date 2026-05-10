from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

def home(request):
    query = request.GET.get('q')

    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 3)  # sayfa başına 3 post
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'create.html', {'form': form})


def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'update.html', {'form': form})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('home')
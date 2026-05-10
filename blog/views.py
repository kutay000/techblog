from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

# 🔍 SEARCH
from django.db.models import Q

# 🔐 AUTH
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# 🏠 HOME + SEARCH + PAGINATION
def home(request):
    query = request.GET.get('q')

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 3)  # sayfa başına 3 post
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'home.html', {'page_obj': page_obj})


# 📄 DETAIL
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'detail.html', {'post': post})


# ➕ CREATE (LOGIN ZORUNLU)
@login_required
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


# ✏️ UPDATE (SADECE KENDİ POSTU)
@login_required
def update_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'update.html', {'form': form})


# ❌ DELETE (SADECE KENDİ POSTU)
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('home')

    post.delete()
    return redirect('home')


# 🔐 REGISTER
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})
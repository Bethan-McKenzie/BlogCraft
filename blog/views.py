from blog.forms import EditProfileForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone

from blog.forms import PostForm
from blog.forms import CommentForm
from blog.models import blog

def home(request):
    posts = blog.objects.all()
    
    return render(request, 'blog/home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.post)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.User
            blog.published_on = timezone.now()
            blog.save()
            return redirect('post_detail', slug=slug)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def my_profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'blog/my_profile.html', context)


def detail(request, slug):
    post = get_object_or_404(blog, slug=slug)
    comments = post.blog_comments.all()
    comment_count = post.blog_comments.count()
    print("I am comments", comments)


    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()


    return render(request, 'blog/detail.html', {'post': post, 'form': form, 'comments': comments, 'comment_count': comment_count})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('https://8000-bethanmckenzi-blogcraft-ku1kzwexrtm.ws-eu110.gitpod.io/my_profile/')

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'blog/edit_profile.html', args)
from blog.forms import EditProfileForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from blog.forms import EditProfileForm
from blog.forms import PostForm
from blog.forms import CommentForm
from blog.models import blog

def home(request):
    posts = blog.objects.all()
    context = {
        'posts': posts,
        'slug': blog.slug
        }
    return render(request, 'blog/home.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.published_on = timezone.now()
            if not blog.slug:
                blog.slug = slugify(blog.title)
            blog.save()
            return redirect('detail', slug=blog.slug)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def my_profile(request):
    context = {'user': request.user}
    return render(request, 'blog/my_profile.html', context)


def detail (request, slug):
    post = get_object_or_404(blog, slug=slug)
    comments = post.blog_comments.all()
    comment_count = post.blog_comments.count()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('detail.html', slug=slug)
    else:
        form = CommentForm()


    return render(request, 'blog/detail.html', {'post': post, 'form': form, 'comments': comments, 'comment_count': comment_count})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_profile'))

    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'blog/edit_profile.html', args)

def delete_post(request,slug):
    """
    Allows a logged in user to delete their own posts in post_detail, also allows a superuser to delete any post from the post_detail
    """
    post = get_object_or_404(blog, slug=slug)
    if request.user == post.author or request.user.is_superuser:
        if request.method =="POST":
        # delete post
            post.delete()
            # after deleting redirect to 
            # home page
            messsages.success(request, f"Successfully deleted.")
        else:
            messages.success(request, f"Post not deleted.")
        return HttpResponseRedirect('/')

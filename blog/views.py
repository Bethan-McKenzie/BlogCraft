from django.shortcuts import get_object_or_404, render

from blog.models import blog

def home(request):
    posts = blog.objects.all()
    
    return render(request, 'blog/home.html', {'posts': posts})

def create_post(request):
    return render(request, 'blog/create_post.html')

def my_profile(request):
    return render(request, 'blog/my_profile.html')


def detail(request, slug):
    post = get_object_or_404(blog, slug=slug)

    return render(request, 'blog/detail.html', {'post': post})
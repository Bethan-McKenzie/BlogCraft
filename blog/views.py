from django.shortcuts import render

from blog.models import blog

def home(request):
    posts = blog.objects.all()
    
    return render(request, 'blog/home.html', {'posts': posts})

def create_post(request):
    return render(request, 'blog/create_post.html')

def my_profile(request):
    return render(request, 'blog/my_profile.html')
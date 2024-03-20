from django.shortcuts import render

def index(request):
    return render(request, 'blog/index.html')

def create_post(request):
    return render(request, 'blog/create_post.html')

def my_profile(request):
    return render(request, 'blog/my_profile.html')
from django.shortcuts import get_object_or_404, redirect, render

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
    return render(request, 'blog/my_profile.html')


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
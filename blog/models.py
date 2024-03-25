from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_on = models.DateTimeField(default=timezone.now)
    description = models.TextField(max_length=250)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    keywords = models.CharField(max_length=200, blank=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    comments = models.ManyToManyField(User, related_name='blog_comments', blank=True)

class Comment(models.Model):
    post = models.ForeignKey(blog, related_name='blog_comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    published_on = models.DateTimeField(default=timezone.now)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True)
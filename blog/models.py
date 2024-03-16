from django.db import models
from cloudinary.models import CloudinaryField


class blog(models.Model):
    title = models.CharField(max_length=100)
    published_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=250)
    image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    keywords = models.CharField(max_length=200, blank=True)
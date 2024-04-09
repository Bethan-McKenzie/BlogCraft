from django.contrib import admin
from django.urls import path, include

from blog.views import create_post
from blog.views import home
from blog.views import my_profile
from blog.views import edit_profile
from blog.views import detail

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('create_post/', create_post, name='create_post'),
    path('my_profile/', my_profile, name='my_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('<slug:slug>/', detail, name='detail'),
    path('', include('blog.urls')),
    path('', home, name='home'),
]

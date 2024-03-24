from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post')
]
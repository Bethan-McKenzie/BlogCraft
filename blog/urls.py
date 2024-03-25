from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
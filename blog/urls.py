from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.create_post, name='create_post'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('my_profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('<slug:slug>/', views.detail, name='detail'),
    path('slug:slug>/delete/', views.delete_post, name='delete_post'),
    path(r'', views.home),
]
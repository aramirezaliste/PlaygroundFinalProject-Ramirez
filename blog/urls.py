
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/<int:id>', views.edit_post, name='edit_post'),
    path('create_post/', views.create_post, name='create_post'),

]


from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('posts/', views.posts_list, name='posts_list'),
    path('posts/edit/<int:id>', views.edit_post, name='post_edit'),
    path('posts/remove/<int:id>', views.remove_post, name='remove_post'),
    path('create_post/', views.create_post, name='create_post'),
    path('posts/detail/<int:id>', views.detail_post, name='detail_post')

]

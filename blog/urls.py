
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog-home/', views.blog_home, name='blog_home'),
    path('search-in-blogs/', views.bs, name='bs'),
    path('all-blogs/<str:pk>/', views.cat_list, name='cat_list'),
    path('blogs/<str:pk>/', views.blog_detail, name='blog_detail'),
] 

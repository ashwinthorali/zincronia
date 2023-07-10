from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('logout-user/', views.byebye, name='byebye'),
    
] 
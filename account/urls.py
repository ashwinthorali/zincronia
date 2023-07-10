from django.urls import path
from . import views
app_name='account'

urlpatterns = [
    path('login-user/', views.login_user, name='login_user'),
    path('create-user/', views.createuser, name='createuser'),
    path('checkup', views.checkup, name='checkup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('change-password/', views.changepw, name='changepw'),
    
] 
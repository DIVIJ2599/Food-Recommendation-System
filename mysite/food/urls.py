from django.contrib import admin
from django.urls import path,include
from food import views
urlpatterns = [
    path('',views.index,name='index'),
    path('menu.html',views.menu,name='menu'),
    path('about.html',views.about,name='about'),
    path('index.html',views.index,name='index'),
    path('login.html',views.login,name='login'),
    path('signup.html',views.signup,name='signup'),
]
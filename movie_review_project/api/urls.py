from django.urls import path 
from .views import welcome 
from django.urls import path
from .views import welcome, movie_list, review_list_create, register
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('welcome/', welcome),
    path('movies/', movie_list),
    path('movies/<int:movie_id>/reviews/', review_list_create),
    path('register/', register),
    path('login/', obtain_auth_token), # DRF's built-in login view
]

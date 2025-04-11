from django.urls import path 
from .views import welcome 
from django.urls import path
from .views import welcome, movie_list
from django.contrib import admin
from django.urls import path, include


# urlpatterns = [ 
#     path('', welcome), 
# ] 



urlpatterns = [
    path('welcome/', welcome),
    path('movies/', movie_list),
]
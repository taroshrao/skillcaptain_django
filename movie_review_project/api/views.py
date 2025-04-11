from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
 
def welcome(request): 
    return JsonResponse({
        "message": "Welcome to the Movie Review API!"
        })



@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all() #get all movies
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
from django.shortcuts import render

# Create your views here.
from .models import Review
from .serializers import ReviewSerializer
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

@api_view(['GET', 'POST'])
def review_list_create(request, movie_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie_id=movie_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data.copy()
        data['movie'] = movie_id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

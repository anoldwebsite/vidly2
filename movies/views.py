from ntpath import join
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie

# Create your views here.
def index(request):
  # The methods below represent our Data Abstraction API and under the hood generate SQL queries automatically for us.
  movies = Movie.objects.all()  # SELECT * FROM movies_movie
  # Movie.objects.filter(release_year=1984)  # SELECT * FROM movies_movie WHERE release_year=1984
  # Movie.objects.get(id=1)  # SELECT * FROM movies_movie WHERE id=1 
  # output = ', '.join([m.title for m in movies])  # joinin the list and putting comman between elements to get a string.
  # return HttpResponse(output)
  return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    # The first argument Movie tells about the model to use. At the moment we have two models i.e. Movie and Genre in our movie app.
    movie = get_object_or_404(Movie, pk=movie_id)  # get_object_or_404(Movie, id=movie_id) will also work.
    return render(request, 'movies/detail.html', {'movie': movie})
"""
    # The following code solved the problem of movie id that we don't have but 
    # in django we have a short cut to do the same and it is to use get_object_or_404 as shown above.
    try:
      movie = Movie.objects.get(pk=movie_id)  # Movie.objects.get(id=movie_id) will also work.
      return render(request, 'movies/detail.html', {'movie': movie})
    except Movie.DoesNotExist: # Movie inherits DoesNotExist class from its super class models.Model
      raise Http404()
"""




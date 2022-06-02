import imp
from unicodedata import name
from django.urls import path
from . import views

app_name = "movies"  # According to the conventions of the django framework, app_name is a known variable name and pointing it to movies, django knows that we are talking about this app movies in file index.html when we refer to movies:detail

urlpatterns = [
  path('', views.index, name='index'),
  # path('', views.index, name='movies_index'),
  path('<int:movie_id>', views.detail, name='detail')  # movies/1  or movies/2  i.e. movies/id
  # path('<int:movie_id>', views.detail, name='movies_detail')  # movies/1  or movies/2  i.e. movies/id
  # int: before movie_id aboe ensures that the app gives suitable error message if a non-numeric movie_id is passed in the url in address bar.
]
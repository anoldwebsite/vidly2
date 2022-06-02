from django.contrib import admin
from django.urls import path, include
from api.models import MovieResource
from . import views

movie_resource = MovieResource()  # Creating an instance of the MovieResource imported above.

urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('api/', include(movie_resource.urls))  # movie_resource object has a property which will return a URL, the value of which is based on resource_name = 'movies' in the class MovieResource. 
]

from django.db import models
from pkg_resources import resource_filename
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.
# We don't want to name the class as Movie as we want to differentiate it from the class Movie in our model.py in the app movies.
class MovieResource(ModelResource):
  # tastypie frameworks looks for an inner class Meta which has meta data about our movies.
  class Meta:
    queryset = Movie.objects.all()  # Returns a query object. Lazy loading. Does not return all movies right now. Will be loaded sometimes in future when needed.
    resource_name = 'movies'  # This means that we will have this word in the end point i.e. URL e.g. our-domain_name/api/movies
    excludes = ['date_Created']  # This does not need to be shown to customers/users/consumers of API, so we exclude it.
    









# Through an api end point, you expose some resources to the world for consumption.
# REST stands for representational state transfer. It deals with how applications should talk to one another over http protocol. Search it for more details.

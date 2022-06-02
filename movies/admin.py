from django.contrib import admin
from .models import Genre, Movie

class GenreAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
  # fields = ('title', 'genre')
  # If you want to exclude one field from your table then use exclude
  exclude = ('date_created', ) # The comma is to tell python that it is a tuple otherwise it will be confused with a string.
  list_display = ('title', 'number_in_stock', 'daily_rate')
  # list_display = ('title', 'genre', 'number_in_stock', 'daily_rate')


# Register your models here.
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)

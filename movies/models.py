from tkinter import CASCADE
from django.db import models
from django.utils import timezone

# Create your models here.
class Genre(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):  # This returns string representation of a Genre object.
    return self.name

class Movie(models.Model):
  title = models.CharField(max_length=255)
  release_year = models.IntegerField()
  number_in_stock = models.IntegerField()
  daily_rate = models.FloatField()
  genre = models.ForeignKey(Genre, on_delete=models.CASCADE)  # If some genre is deleted, all the movies from that genres will also be deleted.
  date_Created = models.DateTimeField(default=timezone.now)  # Do not use () after now otherwise the current date and time will be hardcoded in the migration. Pass only reference.



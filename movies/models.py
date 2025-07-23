from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    imdbID = models.CharField(max_length=20, unique=True)
    poster = models.URLField(max_length=500, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    director = models.CharField(max_length=255, blank=True)
    actors = models.CharField(max_length=255, blank=True)
    plot = models.TextField(blank=True)
    language = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    released = models.CharField(max_length=50, blank=True)
    runtime = models.CharField(max_length=50, blank=True)
    writer = models.CharField(max_length=255, blank=True)
    awards = models.CharField(max_length=255, blank=True)
    box_office = models.CharField(max_length=100, blank=True)
    production = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    imdb_rating = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

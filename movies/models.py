from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=10)
    imdbID = models.CharField(max_length=20, unique=True)
    poster = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.year})"

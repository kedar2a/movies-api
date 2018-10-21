from django.db import models

'''
Example:
{
    "99popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz"
  }

Analysis:
- 5 fields in each document.
- 3 entities
    - director
    - genre
    - movie
'''

class MovieDirector(models.Model):
    director = models.CharField(max_length=30, unique=True)

    class Meta:
        verbose_name='Director'

    def __str__(self):
        return self.director


class MovieGenre(models.Model):
    genre = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name='Genre'

    def __str__(self):
        return self.genre


class Movie(models.Model):
    """docstring for Movies"""
    name = models.CharField(max_length=30, unique=True)
    director = models.ForeignKey(MovieDirector, on_delete=models.CASCADE)
    genre = models.ManyToManyField(MovieGenre)
    popularity99 = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='99popularity')  # "99popularity": 83.0,
    imdb_score = models.DecimalField(max_digits=2, decimal_places=1)  # "imdb_score": 8.3,

    class Meta:
        verbose_name='Movie'

    def __str__(self):
        return self.name

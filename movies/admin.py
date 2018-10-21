from django.contrib import admin
from .models import MovieDirector, MovieGenre, Movie

admin.site.register(Movie)
admin.site.register(MovieDirector)
admin.site.register(MovieGenre)
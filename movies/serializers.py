from rest_framework import serializers
from .models import MovieDirector, MovieGenre, Movie


class DirectorSerializer(serializers.ModelSerializer):
    director = serializers.StringRelatedField(many=True)

    class Meta:
        model = MovieDirector
        fields = ('director')


class GenreSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)

    class Meta:
        model = MovieGenre
        fields = ('genre')



class MovieListSerializer(serializers.ModelSerializer):
    director = serializers.SlugRelatedField(
        read_only=True,
        slug_field='director'
     )
    genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='genre'
     )

    class Meta:
        model = Movie
        fields = ('name', 'director', 'genre', 'popularity99', 'imdb_score')


class MovieCreateSerializer(serializers.ModelSerializer):
    director = serializers.CharField()
    genre = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Movie
        fields = ('name', 'director', 'genre', 'popularity99', 'imdb_score')

    # def validate_director(self, value):
    #     return value

    def create(self, validated_data):
        director = validated_data.pop('director')
        dir_obj = MovieDirector.objects.get_or_create(director=director.strip())
        validated_data['director'] = dir_obj[0]
        genre_list = validated_data.pop('genre')
        instance = Movie.objects.create(**validated_data)
        # needs to raise/handle unique contraint error
        for genre in genre_list[0].split(','):
            genre_obj = MovieGenre.objects.get_or_create(genre=genre.strip())
            instance.genre.add(genre_obj[0])

        return instance

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import Movie
from .serializers import MovieCreateSerializer, MovieListSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    CRUD operations handler
    """
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer


    @staticmethod
    def format_data(data, calling_method):
        def _arrange_keys(data_dict):
            return {k if k != 'popularity99' else '99popularity': v for k, v in data_dict.items()}
            
        if calling_method == 'retrieve':
            return _arrange_keys(data)

        if calling_method == 'list':
            return [_arrange_keys(i) for i in data]


    def list(self, request, *arg, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        serializer = MovieListSerializer(queryset, many=True)

        return Response(self.format_data(data=serializer.data, calling_method='list'))


    def retrieve(self, request, *arg, **kwargs):
        movie = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = MovieListSerializer(movie)

        return Response(self.format_data(data=serializer.data, calling_method='retrieve'))


    def create(self, request, *arg, **kwargs):
        print (request)
        permission_classes = (IsAdminUser)
        req_data = request.data.copy()
        req_data['popularity99'] = request.data['99popularity']
        write_serializer = MovieCreateSerializer(data=req_data)
        write_serializer.is_valid(raise_exception=False)
        instance = self.perform_create(write_serializer)
        read_serializer = MovieListSerializer(instance)

        return Response(read_serializer.data)

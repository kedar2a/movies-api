from django.db.models import Q
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import filters

from .models import Movie
from .serializers import MovieCreateSerializer, MovieListSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    CRUD operations handler
    """
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('name')
    filter_backends = (filters.SearchFilter,)
    # search_fields = ('name', 'director', 'genre', '99popularity', 'imdb_score', '')

    def get_queryset(self):
        queryset = Movie.objects.all()
        search_str = self.request.query_params.get('search', None)
        if search_str is not None:
            queryset = Movie.objects.filter(Q(name__icontains=search_str) \
                | Q(genre__genre__icontains=search_str) \
                | Q(director__director__icontains=search_str) \
                # | Q(imdb_score=search_str) \
                # | Q(popularity99=search_str) \
                )
        return queryset

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
        serializer = MovieListSerializer(queryset, many=True)

        return Response(self.format_data(data=serializer.data, calling_method='list'))


    def retrieve(self, request, *arg, **kwargs):
        movie = get_object_or_404(self.queryset, pk=kwargs['pk'])
        serializer = MovieListSerializer(movie)

        return Response(self.format_data(data=serializer.data, calling_method='retrieve'))


    def create(self, request, *arg, **kwargs):
        permission_classes = (IsAdminUser)
        req_data = request.data.copy()
        req_data['popularity99'] = request.data['99popularity']
        write_serializer = MovieCreateSerializer(data=req_data)
        write_serializer.is_valid(raise_exception=False)
        instance = self.perform_create(write_serializer)
        read_serializer = MovieListSerializer(instance)

        return Response(read_serializer.data)


    # needs to rework with proper understanding
    # def update(self, request, pk=None, *arg, **kwargs):
    #     permission_classes = (IsAdminUser)
    #     req_data = request.data.copy()
    #     try:
    #         req_data['popularity99'] = request.data['99popularity']
    #     except Exception as e:
    #         pass
    #     # print(req_data)
    #     write_serializer = MovieCreateSerializer(data=req_data)
    #     write_serializer.is_valid(raise_exception=False)
    #     instance = self.perform_create(write_serializer)
    #     read_serializer = MovieListSerializer(instance)
    #     return Response(read_serializer.data)

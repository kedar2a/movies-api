from django.urls import path
from .views import MovieViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'movies', MovieViewSet, basename='movie')
urlpatterns = router.urls

# urlpatterns = [
# 	path('movies/', MovieViewSet.as_view(), name='all_movies')
# ]
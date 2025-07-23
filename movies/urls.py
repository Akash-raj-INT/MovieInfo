from django.urls import path
from .views import MovieListCreateAPIView, MovieRetrieveAPIView

urlpatterns = [
    path('api/movies/', MovieListCreateAPIView.as_view(), name='api-movie-list-create'),
    path('api/movies/<int:id>/', MovieRetrieveAPIView.as_view(), name='api-movie-detail'),
] 
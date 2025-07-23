from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_movie, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('history/', views.personal_history, name='personal_history'),
    path('register/', views.register, name='register'),
    path('movie/<str:imdb_id>/', views.movie_detail, name='movie_detail'),
]


import requests
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer

@login_required
def search_movie(request):
    movie_data = {}
    # Get search history from session, or initialize as empty list
    search_history = request.session.get('search_history', [])

    if 'title' in request.GET:
        title = request.GET['title']
        url = f"http://www.omdbapi.com/?apikey=316fa37d&t={title}"
        response = requests.get(url)
        movie_data = response.json()
        # Add to history if not already present
        if title and title not in search_history:
            search_history.insert(0, title)  # Most recent first
            # Limit history to last 10 searches
            search_history = search_history[:10]
            request.session['search_history'] = search_history

    return render(request, 'movies/search.html', {
        'movie_data': movie_data,
        'search_history': search_history
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})

@login_required
def personal_history(request):
    search_history = request.session.get('search_history', [])
    return render(request, 'movies/personal_history.html', {'search_history': search_history})

def dashboard(request):
    # Show Bollywood movies using a Bollywood-related OMDb API query
    url = "http://www.omdbapi.com/?apikey=316fa37d&s=dil&type=movie"
    response = requests.get(url)
    movies = []
    if response.status_code == 200:
        data = response.json()
        if data.get('Response') == 'True':
            movies = data.get('Search', [])
    return render(request, 'movies/dashboard.html', {'movies': movies})

def movie_detail(request, imdb_id):
    url = f"http://www.omdbapi.com/?apikey=316fa37d&i={imdb_id}&plot=full"
    response = requests.get(url)
    movie = {}
    if response.status_code == 200:
        movie = response.json()
    return render(request, 'movies/movie_detail.html', {'movie': movie})

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'id'

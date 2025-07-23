from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie

@login_required
def search_movie(request):
    movie_data = None
    search_history = request.session.get('search_history', [])

    if 'title' in request.GET:
        title = request.GET['title']
        try:
            movie = Movie.objects.get(title__iexact=title)
            movie_data = {
                'Title': movie.title,
                'Year': movie.year,
                'imdbID': movie.imdbID,
                'Poster': movie.poster,
                'imdbRating': movie.imdb_rating,
                'Plot': movie.plot,
                'Actors': movie.actors,
            }
        except Movie.DoesNotExist:
            movie_data = None
        if title and title not in search_history:
            search_history.insert(0, title)
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
    # Show all movies from the local database
    movies = Movie.objects.all()
    movie_list = []
    for movie in movies:
        movie_list.append({
            'Title': movie.title,
            'Year': movie.year,
            'imdbID': movie.imdbID,
            'Poster': movie.poster,
        })
    return render(request, 'movies/dashboard.html', {'movies': movie_list})


def movie_detail(request, imdb_id):
    # Get movie from local database
    try:
        movie = Movie.objects.get(imdbID=imdb_id)
        movie_data = {
            'Title': movie.title,
            'Year': movie.year,
            'imdbID': movie.imdbID,
            'Poster': movie.poster,
            'Genre': movie.genre,
            'Director': movie.director,
            'Actors': movie.actors,
            'Plot': movie.plot,
            'Language': movie.language,
            'Country': movie.country,
            'Released': movie.released,
            'Runtime': movie.runtime,
            'Writer': movie.writer,
            'Awards': movie.awards,
            'BoxOffice': movie.box_office,
            'Production': movie.production,
            'Website': movie.website,
            'imdbRating': movie.imdb_rating,
        }
    except Movie.DoesNotExist:
        movie_data = None
    return render(request, 'movies/movie_detail.html', {'movie': movie_data})

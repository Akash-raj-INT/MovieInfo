"""
URL configuration for movieinfo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.search_movie, name='search_movie'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('history/', views.personal_history, name='personal_history'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('movie/<imdb_id>/', views.movie_detail, name='movie_detail'),
    path('', include('movies.urls')),  # Add this line to include API URLs
]


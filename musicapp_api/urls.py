from django.urls import re_path as url
from django.urls import path, include
from .views import (
    ArtistApiView,SongApiView,SongIdApiView
)

urlpatterns = [
    path('api', ArtistApiView.as_view()),
    path('songapi', SongApiView.as_view()),
    path('songapi/<int:song_id>/', SongIdApiView.as_view()),
]

from rest_framework import serializers
from .models import Artist, Song, Lyric

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id", "first_name", "last_name", "age"]

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["id", "title", "date_released", "likes", "artist_id"]

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = ["id", "content", "song_id"]

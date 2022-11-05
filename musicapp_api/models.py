from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateTimeField()
    likes = models.IntegerField()
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Lyric(models.Model):
    content = models.TextField()
    song_id =  models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song_id

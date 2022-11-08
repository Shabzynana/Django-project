from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Artist, Song, Lyric
from .serializers import ArtistSerializer, SongSerializer, LyricSerializer



class ArtistApiView(APIView):
    
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
       
        artist = Artist.objects.all().values()
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
       
        data = {
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'age': request.data.get('age')
        }
        serializer = ArtistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SongApiView(APIView):

    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
       
        data = {
            'title': request.data.get('title'),
            'date_released': request.data.get('date_released'),
            'likes': request.data.get('likes'),
            'artist_id': request.data.get('artist_id')
        }
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SongIdApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, song_id):

        try:
            return Song.objects.get(id=song_id)
        except Song.DoesNotExist:
            return None

    def get(self, request, song_id, *args, **kwargs):

        song = self.get_object(song_id)
        if not song:
            return Response(
                {"res": "Object with song id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, song_id, *args, **kwargs):

        song = self.get_object(song_id)
        if not song:
            return Response(
                {"res": "Object with song id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'title': request.data.get('title'),
            'date_released': request.data.get('date_released'),
            'likes': request.data.get('likes'),
            'artist_id': request.data.get('artist_id')
        }
        serializer = SongSerializer(instance = song, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, song_id, *args, **kwargs):

        song = self.get_object(song_id)
        if not song:
            return Response(
                {"res": "Object with song id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        song.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

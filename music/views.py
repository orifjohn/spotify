from rest_framework.views import APIView
from rest_framework.response import Response
from music.models import Song, Movie
from music.serializers import SongSerializer, MovieSerializer


class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(data=serializer.data)


class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

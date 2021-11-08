from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from music.models import Song, Album, Artist
from music.serializers import SongSerializer, AlbumSerializer, ArtistSerializer


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = LimitOffsetPagination


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=True, methods=["GET"])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = AlbumSerializer(artist.album_set.all(), many=True)

        return Response(serializer.data)

# class SongAPIView(APIView):
#     def get(self, request):
#         songs = Song.objects.all()
#         serializer = SongSerializer(songs, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = SongSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         serializer.save()
#
#         return Response(data=serializer.data)
#
#
# class MovieAPIView(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

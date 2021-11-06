from rest_framework.views import APIView
from rest_framework.response import Response
from music.models import Song
from music.serializers import SongSerializer


class SongAPIView(APIView):
    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)

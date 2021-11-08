from rest_framework import serializers
from .models import Song, Album, Artist, Movie
from rest_framework.validators import ValidationError


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'cover', 'source')

    def validate_source(self, value):
        if not value.endswith('.mp3'):
            raise ValidationError(detail="Mp3 file is required")

        return value


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

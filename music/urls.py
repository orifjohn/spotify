from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SongViewSet, AlbumViewSet, ArtistViewSet, MovieViewSet

router = DefaultRouter()
router.register('songs', SongViewSet)
router.register("albums", AlbumViewSet)
router.register("artists", ArtistViewSet)
router.register('movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

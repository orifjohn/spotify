from django.urls import path
from .views import SongAPIView, MovieAPIView

urlpatterns = [
    path('song/', SongAPIView.as_view(), name='song'),
    path('movie/', MovieAPIView.as_view(), name='movie'),
]

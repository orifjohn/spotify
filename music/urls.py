from django.urls import path
from .views import SongAPIView

urlpatterns = [
    path('song/', SongAPIView.as_view(), name='song'),
]

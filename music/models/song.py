from django.db import models


class Song(models.Model):
    album = models.ForeignKey('music.Album', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    cover = models.URLField(blank=True)
    source = models.URLField(blank=False, null=False)
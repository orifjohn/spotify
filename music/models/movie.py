from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=150)
    value = models.IntegerField()

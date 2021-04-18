from rest_framework import viewsets
from . import models
from . import serializers

class MovieViewset(viewsets.ModelViewSet):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializer

from django.shortcuts import render
from rest_framework import viewsets
from .models import Singer, Song
from .serializers import SingerSerializer, SongSerializer


class SingerModelViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongModelViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

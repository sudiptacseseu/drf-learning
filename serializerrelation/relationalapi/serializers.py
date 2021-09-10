from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    # Returns name
    # songs = serializers.StringRelatedField(many=True, read_only=True)
    # Returns id
    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Returns hyperlinked id
    # songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # Returns field based value
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # Returns hyperlinked id
    # songs = serializers.HyperlinkedIdentityField(view_name='song-detail')

    # Nested serializer to display songs with details
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs']



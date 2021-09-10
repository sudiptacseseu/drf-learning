from rest_framework import serializers
from .models import Singer, Song


class SingerSerializer(serializers.ModelSerializer):
    # Returns name
    song = serializers.StringRelatedField(many=True, read_only=True)
    # Returns id
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Returns hyperlinked id
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail')
    # Returns field based value
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # Returns hyperlinked id
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']


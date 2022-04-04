from rest_framework import serializers
from .models import Posts, Comments, Albums


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['userId', 'id', 'title', 'body']


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        fields = ['postId', 'id', 'name', 'email', 'body']


class AlbumsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums
        fields = ['userId', 'id', 'title']


class PhotosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums
        fields = ['albumId', 'id', 'title', 'url', 'thumbnailUrl']


class TodosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Albums
        fields = ['userId', 'id', 'title', 'completed']
        

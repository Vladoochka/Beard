from rest_framework import generics
from . import serializers
from .models import Posts, Comments, Albums, Todos, Photos
from django.shortcuts import render


class PostsList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = serializers.PostsSerializer


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = serializers.PostsSerializer


class CommentsList(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentsSerializer


class CommentsDetail(generics.RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentsSerializer


class AlbumsList(generics.ListAPIView):
    queryset = Albums.objects.all()
    serializer_class = serializers.AlbumsSerializer


class PhotosList(generics.ListAPIView):
    queryset = Photos.objects.all()
    serializer_class = serializers.PhotosSerializer


class TodosList(generics.ListAPIView):
    queryset = Todos.objects.all()
    serializer_class = serializers.TodosSerializer


def home(request):
    return render(request, 'home.html', {'title': 'Главная страница сайта'})

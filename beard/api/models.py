from django.db import models


class Posts(models.Model):
    userId = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)


class Comments(models.Model):
    postId = models.ForeignKey('Posts', related_name='comments', on_delete=models.PROTECT)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    body = models.CharField(max_length=500)


class Albums(models.Model):
    userId = models.ForeignKey('Posts', related_name='albums', on_delete=models.PROTECT)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)


class Photos(models.Model):
    albumId = models.ForeignKey('Albums', related_name='photos', on_delete=models.PROTECT)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    thumbnailUrl = models.CharField(max_length=100)


class Todos(models.Model):
    userId = models.ForeignKey('Posts', related_name='todos', on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)





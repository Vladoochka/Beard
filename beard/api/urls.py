from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('posts/', views.PostsList.as_view()),
    path('posts/<int:pk>/', views.PostsDetail.as_view()),
    path('comments/', views.CommentsList.as_view()),
    path('posts/<int:pk>/comments', views.CommentsDetail.as_view()),
    path('comments/?postId=<int:pk>', views.CommentsDetail.as_view()),
    path('albums/', views.CommentsList.as_view()),
    path('photos/', views.PhotosList.as_view()),
    path('todos/', views.TodosList.as_view()),
    path('', views.home),

]

urlpatterns = format_suffix_patterns(urlpatterns)
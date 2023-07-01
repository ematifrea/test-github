from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostSerializer, PostDetailSerializer


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list_with_bootstrap.html', {'posts': posts})
    # return render(request, 'post_list.html', {'posts': posts})


class PostViewSet(ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.filter(published_date__isnull=False)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostList(ListCreateAPIView):
    queryset = Post.objects.filter(published_date__isnull=False)
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(published_date__isnull=False)
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

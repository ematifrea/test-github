from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'created_date', 'published_date')


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"

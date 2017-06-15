from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'postedBy', 'headerImg', 'imgClass', 'content', 'postedAt')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('postId', 'commentId', 'postedBy', 'content', 'postedAt')

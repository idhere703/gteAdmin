from rest_framework import serializers
from .models import Post, Comment, User, Like


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'postedBy', 'headerImg', 'imgClass', 'content', 'postedAt')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('postId', 'commentId', 'postedBy', 'content', 'postedAt')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('userId', 'firstName', 'lastName', 'email', 'phone')

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like
        fields = ('createdBy', 'createdAt', 'postId', 'like')
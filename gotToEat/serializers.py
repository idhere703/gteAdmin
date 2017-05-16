from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'postedBy', 'headerImg', 'imgClass', 'content', 'postedAt')
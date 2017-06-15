# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets



def index(request):
    return HttpResponse("You're at the index.")

class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-postedAt')
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-postedAt')
    serializer_class = CommentSerializer

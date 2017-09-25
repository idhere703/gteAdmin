# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Post, Comment, User
from .serializers import PostSerializer, CommentSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import permissions


def index(request):
    return HttpResponse("You're at the index.")

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-postedAt')
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-postedAt')
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-postedAt')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

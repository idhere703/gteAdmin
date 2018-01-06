# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class State(models.Model):
    postalCode = models.TextField(max_length=2)
    name = models.TextField(max_length=200)
    allowedSignup = models.BooleanField()
    def __str__(self):
        return self.name


class User(models.Model):
    userId = models.TextField(max_length=100)
    firstName = models.TextField(max_length=200)
    lastName = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.TextField(max_length=200)
    city = models.TextField(max_length=200)
    state = models.ForeignKey(
        'State',
        on_delete=models.CASCADE,
    )
    zip = models.TextField(max_length=5)
    country = models.TextField(max_length=200)
    def __str__(self):
        return self.email


class Post(models.Model):
    title = models.TextField(max_length=100)
    subtitle = models.TextField(max_length=200)
    postedBy = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    imgClass = models.TextField(max_length=100)
    headerImg = models.FileField(upload_to='uploads/')
    content = models.TextField()
    postedAt = models.DateTimeField('date published')
    def __str__(self):
        return self.title


class Comment(models.Model):
    commentId = models.TextField(max_length=100)
    postId = models.ForeignKey(
        'Post'
    )
    postedBy = models.TextField(max_length=200)
    content = models.TextField()
    postedAt = models.DateTimeField('date published')
    def __str__(self):
        return self.content

class Like(models.Model):
    createdBy = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    createdAt = models.DateTimeField('created at')
    postId = models.ForeignKey(
        'Post'
    )
    like = models.BooleanField()
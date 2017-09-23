# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=100)
    subtitle = models.TextField(max_length=200)
    postedBy = models.TextField(max_length=200)
    imgClass = models.TextField(max_length=100)
    headerImg = models.FileField(upload_to='uploads/')
    content = models.TextField()
    postedAt = models.DateTimeField('date published')
    def __str__(self):
        return self.title


class Comment(models.Model):
    commentId = models.TextField(max_length=100)
    postId = models.TextField(max_length=200)
    postedBy = models.TextField(max_length=200)
    content = models.TextField()
    postedAt = models.DateTimeField('date published')
    def __str__(self):
        return self.content

class User(models.Model):
    userId = models.TextField
    firstName = models.TextField(max_length=200)
    lastName = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.TextField(max_length=200)
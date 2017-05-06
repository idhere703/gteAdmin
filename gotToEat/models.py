# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.TextField(max_length=100)
    subtitle = models.TextField(max_length=200)
    postedBy = models.TextField(max_length=200)
    imgClass = models.TextField(max_length=100)
    content = models.TextField()
    postedAt = models.DateTimeField('date published')
    def __str__(self):
        return self.title
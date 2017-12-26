# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Post, Comment, User, Like

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Like)
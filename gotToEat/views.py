# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the index.")
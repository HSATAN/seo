# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

def index(request):

    return render(request, 'seo/index.html')

def serch(request):

    word = request.GET.get("wd")

    return HttpResponse(word)
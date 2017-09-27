# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *
from .forms import *

# Create your views here.
def index(request):
    context = {
        "posts" : Post.objects.all(),
        "form" : PostForm()
    }
    return render(request, "post/index.html", context)
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            Post.objects.create(post=form.cleaned_data["add_a_note"])
    return render(request, "post/posts.html", {"posts" : Post.objects.all()})
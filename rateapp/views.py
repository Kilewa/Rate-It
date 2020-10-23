from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, User




def home(request):
    # posts = Post.get_all_images()

    # context = {
    #     'posts': posts,
    # }
    return render(request, 'rateapp/home.html')
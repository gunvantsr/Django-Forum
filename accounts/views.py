from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from blog.models import Post
# Create your views here.


def index(request):
    users = User.objects.all()
    return render(request, 'accounts/home.html', {'users':users})

def user_profile(request, username):
    user = User.objects.get(username=username)
    userposts = Post.objects.filter(author__username=username)
    return render(request, 'accounts/profile.html', {'user': user, 'userposts': userposts})
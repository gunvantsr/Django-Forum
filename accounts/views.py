from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.


def index(request):
    users = User.objects.all()
    return render(request, 'accounts/home.html', {'users':users})

def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'accounts/profile.html', {'user': user})
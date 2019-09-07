from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=250, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile.png')
    birthdate = models.DateField(null=True, blank=True)
    twitter_link = models.CharField(max_length=64)
    facebook_link = models.CharField(max_length=64)
    verified = models.BooleanField()

    def __str__(self):
        return str(self.user.username)
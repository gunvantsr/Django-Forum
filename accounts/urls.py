from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='profile-index'),
    path("accounts/<str:username>/", views.user_profile, name='profile'),
    path("<str:username>/", views.user_profile, name='profile')
]


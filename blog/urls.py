from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('login/',LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/',LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('post/new/', views.PostCreateView.as_view(), name='new-post'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
    path('<str:category>/', views.category_post, name='category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

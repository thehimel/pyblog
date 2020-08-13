from django.urls import path
from blog import views

# Always use the trailing slash after every path to avoid confusion.
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

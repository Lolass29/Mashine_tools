from django.urls import path
from my_site.views import my_site_view, profile_view, register

urlpatterns = [
    path('shop/', my_site_view),
    path('profile/', profile_view, name='profile'),
    path('register/', register, name='register'),
]

from django.urls import path
from my_site.views import my_site_view

urlpatterns = [
    path('shop/', my_site_view),
]

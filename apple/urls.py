from django.urls import path

from apple.views import index


urlpatterns = [
    path('', index),
]
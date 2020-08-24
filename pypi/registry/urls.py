from django.urls import path
from .views import index, clean
from django.conf.urls import url

urlpatterns = [
    url(r'((simple|packages)/.*)$', index.ViewSet),
    path('clean', clean.ViewSet),
]

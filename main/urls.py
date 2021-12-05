
from django.conf.urls import url, include
from django.urls import path
from .views import UrlView, RootView
from rest_framework import routers


urlpatterns = [
    path('urls/', UrlView.as_view(), name='UrlView'),
    path('urls/<short_code>', UrlView.as_view(), name='UrlView'),
    path('<short_code>', RootView.as_view(), name='RootView')
    ]
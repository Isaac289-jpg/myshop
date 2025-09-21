"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include  # include lets us connect app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),   # connect the shop app URLs
]

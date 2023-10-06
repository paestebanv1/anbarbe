from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("unews", views.unews),
    path("nunews", views.nunews),
    path("pnews", views.pnews),

]

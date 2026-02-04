from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("dashboard/", permanent=True)),
    path("admin/", admin.site.urls),
    path("api/", include("content_posts.urls")),
    path("dashboard/", views.dashboard, name="dashboard"),
]

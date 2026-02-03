from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    path("", lambda request: JsonResponse({
        "status": "OK",
        "message": "Social Media Content Planner is running"
    })),
    path("admin/", admin.site.urls),
    path("api/", include("content_posts.urls")),
]

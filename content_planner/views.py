from django.shortcuts import render
from content_posts.models import SocialPost
from django.db.models import Count

def dashboard(request):
    context = {
        "total": SocialPost.objects.count(),
        "draft": SocialPost.objects.filter(status="Draft").count(),
        "published": SocialPost.objects.filter(status="Published").count(),
        "by_platform": SocialPost.objects.values("platform").annotate(count=Count("id")),
    }
    return render(request, "dashboard.html", context)

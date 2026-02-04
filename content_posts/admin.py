from django.contrib import admin
from .models import SocialPost

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'platform', 'status', 'created_at']
    list_filter = ['platform', 'status']
    search_fields = ['title', 'content']
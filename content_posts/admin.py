from django.contrib import admin
from .models import SocialPost

@admin.register(SocialPost)
class SocialPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'platform', 'status', 'scheduled_time', 'created_at')
    list_filter = ('platform', 'status')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Avg, Sum
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data.pop("scheduled_time", None)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'])
    def analytics(self, request):
        platform_stats = list(Post.objects.values('platform').annotate(count=Count('id')))
        status_stats = list(Post.objects.values('status').annotate(count=Count('id')))
        engagement_stats = list(Post.objects.values('platform').annotate(avg_engagement=Avg('engagement_score')))
        
        return Response({
            'platform_stats': platform_stats,
            'status_stats': status_stats,
            'engagement_stats': engagement_stats,
            'total_posts': Post.objects.count(),
            'total_engagement': Post.objects.aggregate(total=Sum('engagement_score'))['total'] or 0,
        })
    
    @action(detail=False, methods=['get'])
    def fetch_image(self, request):
        # Return placeholder image for now
        return Response({
            'url': 'https://picsum.photos/800/600',
            'thumbnail': 'https://picsum.photos/400/300',
            'author': 'Placeholder',
            'description': 'Random image'
        })

# pyright: reportAttributeAccessIssue=false
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import SocialPost


class SocialPostTests(APITestCase):
    def setUp(self):
        self.post_data = {
            "title": "My First Post",
            "content": "This is a test post",
            "platform": "instagram",
            "status": "Draft",
            "engagement_score": 10,
        }

        self.post = SocialPost.objects.create(**self.post_data)

        self.list_url = reverse("posts-list")
        self.detail_url = reverse("posts-detail", args=[self.post.id])
        self.analytics_url = reverse("post-analytics")

    def test_create_post(self):
        data = {
            "title": "New Twitter Post",
            "content": "Tweeting about Django",
            "platform": "twitter",
            "status": "Scheduled",
        }

        response = self.client.post(self.list_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SocialPost.objects.count(), 2)
        self.assertEqual(response.data["title"], "New Twitter Post")

    def test_read_list_posts(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_read_single_post(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.post_data["title"])

    def test_update_post(self):
        data = {
            "title": "Updated Title",
            "content": "Updated content",
            "platform": "instagram",
            "status": "Published",
        }

        response = self.client.put(self.detail_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Updated Title")
        self.assertEqual(self.post.status, "Published")

    def test_delete_post(self):
        response = self.client.delete(self.detail_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SocialPost.objects.count(), 0)

    def test_analytics_view(self):
        response = self.client.get(self.analytics_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["total_posts"], 1)
        self.assertEqual(response.data["total_engagement"], 10)
        self.assertIn("platform_stats", response.data)
        self.assertIn("status_stats", response.data)
        self.assertIn("engagement_stats", response.data)    
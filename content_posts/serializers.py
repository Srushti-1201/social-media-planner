from rest_framework import serializers
from .models import SocialPost

class SocialPostSerializer(serializers.ModelSerializer):
    scheduled_time = serializers.DateTimeField(
        required=False,
        allow_null=True,
        input_formats=[
            "%Y-%m-%dT%H:%M",    # HTML5 datetime-local
            "%Y-%m-%d %H:%M",    # Standard
            "%d-%m-%Y %H:%M",    # DD-MM-YYYY HH:MM (User input)
            "%d/%m/%Y %H:%M",    # DD/MM/YYYY HH:MM
            "iso-8601",          # ISO 8601
        ]
    )

    class Meta:
        model = SocialPost
        fields = '__all__'

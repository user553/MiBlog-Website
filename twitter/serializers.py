from django.conf import settings
from rest_framework import serializers
from .models import Tweet

max_length = 240                                           

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['content']

    def validate_content(self, value):
        if len(value) > max_length:
            raise serializers.ValidationError('Oops! This tweet is too long!')
        return value
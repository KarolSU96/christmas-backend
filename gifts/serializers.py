from rest_framework import serializers
from .models import Gift

class GiftSerializer(serializers.ModelSerializer):

        
    class Meta:
        model = Gift
        fields = ['id', 'owner', 'title','description','price', 'image', 'created_at', 'updated_at']
        read_only_fields = ['owner']
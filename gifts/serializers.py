from rest_framework import serializers
from .models import Gift

class GiftSerializer(serializers.ModelSerializer):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    class Meta:
        model = Gift
        fields = ['id', 'owner', 'title','description','price', 'image', 'created_at', 'updated_at']
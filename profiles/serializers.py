from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        return obj.owner == self.context['request'].user
    
    class Meta:
        model = Profile
        fields = ['id', 'owner', 'name', 'image', 'created_at', 'updated_at', 'is_owner']

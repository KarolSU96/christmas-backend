from rest_framework import serializers
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = ['id', 'owner', 'title', 'description', 'image', 'created_at', 'updated_at', 'ingredients', 'is_owner']
    
    def get_is_owner(self, obj):
        return obj.owner == self.context['request'].user
    


from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import RecipeSerializer, IngredientSerializer
from christmas_backend.permissions import IsOwnerOrReadOnly
from .models import Recipe, Ingredient

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ingredients_data = serializer.validated_data.pop('ingredients',[])
        recipe = serializer.save(owner=self.request.user)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredient_data) 

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsOwnerOrReadOnly]
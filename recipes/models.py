from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/',
        default='../recipe-placeholder_kxmalj')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='recipes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def create_recipe(sender, instance, created, **kwargs):
        if created:
            Recipe.objects.create(owner=instance, name=f"{instance.username}'s recipe")

post_save.connect(create_recipe, sender=User)
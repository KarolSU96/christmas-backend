from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import MediaCloudinaryStorage

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True)
    image = models.ImageField(
        upload_to='images/',
        storage=MediaCloudinaryStorage(),
        default='../default_profile_d7stiw'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner.username}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance,name=f"{instance.username}'s profile")


post_save.connect(create_profile, sender=User)

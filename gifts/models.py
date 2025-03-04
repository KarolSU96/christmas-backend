from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage


class Gift(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/',
        storage=MediaCloudinaryStorage(),
        default='../Gift-Placeholder_kivws5')
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


def create_gift(sender, instance, created, **kwargs):
    if created:
        Gift.objects.create(owner=instance, name=f"{instance.username}'s gift")


post_save.connect(create_gift, sender=User)

# Generated by Django 5.1.4 on 2024-12-30 10:00

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_d7stiw', storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='images/'),
        ),
    ]

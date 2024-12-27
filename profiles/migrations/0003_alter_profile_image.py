# Generated by Django 5.1.4 on 2024-12-27 16:32

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='default_profile_d7stiw', max_length=255, verbose_name='image'),
        ),
    ]

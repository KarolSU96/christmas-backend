# Generated by Django 5.1.4 on 2025-01-07 10:22

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0004_alter_gift_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='image',
            field=models.ImageField(default='../Gift-Placeholder_kivws5', storage=cloudinary_storage.storage.MediaCloudinaryStorage(), upload_to='images/'),
        ),
    ]

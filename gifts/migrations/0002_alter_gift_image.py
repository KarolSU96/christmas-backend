# Generated by Django 5.1.4 on 2025-01-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='image',
            field=models.ImageField(default='../Gift-Placeholder_kivws5', upload_to='images/'),
        ),
    ]

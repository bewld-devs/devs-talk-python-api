# Generated by Django 4.1.1 on 2022-11-09 12:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devs_talk_api_app', '0023_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cover_photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
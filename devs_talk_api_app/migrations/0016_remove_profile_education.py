# Generated by Django 4.1.1 on 2022-10-19 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devs_talk_api_app', '0015_remove_profile_education_remove_profile_work_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
    ]
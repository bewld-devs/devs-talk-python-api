# Generated by Django 4.1.1 on 2022-10-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs_talk_api_app', '0012_alter_work_responsibilities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='work',
        ),
        migrations.AddField(
            model_name='profile',
            name='work',
            field=models.ManyToManyField(blank=True, null=True, to='devs_talk_api_app.work'),
        ),
    ]
# Generated by Django 4.1.1 on 2022-10-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs_talk_api_feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

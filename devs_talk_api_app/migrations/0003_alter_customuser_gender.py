# Generated by Django 4.1.1 on 2022-09-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs_talk_api_app', '0002_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'MALE'), ('Female', 'FEMALE'), ('Nonbinary', 'NONBINARY'), ('N/A', 'N/A')], max_length=55, null=True),
        ),
    ]
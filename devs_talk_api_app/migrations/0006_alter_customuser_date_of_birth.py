# Generated by Django 4.1.1 on 2022-10-13 20:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs_talk_api_app', '0005_rename_d_o_b_customuser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.date.today, max_length=8, null=True),
        ),
    ]
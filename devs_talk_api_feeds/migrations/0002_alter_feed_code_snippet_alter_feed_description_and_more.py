# Generated by Django 4.1.1 on 2022-10-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devs_talk_api_feeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='code_snippet',
            field=models.TextField(blank=True, max_length=520, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='description',
            field=models.TextField(blank=True, max_length=520, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='language',
            field=models.CharField(blank=True, choices=[('Vue', 'VUE'), ('Python', 'PYTHON'), ('Javascript', 'JAVASCRIPT'), ('Ruby', 'RUBY'), ('Java', 'JAVA'), ('Rails', 'RAILS'), ('React', 'REACT'), ('Angular', 'ANGULAR'), ('Php', 'PHP'), ('Laravel', 'Laravel')], max_length=155, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]

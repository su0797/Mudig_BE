# Generated by Django 4.2.7 on 2023-11-17 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_music_singer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='singer',
        ),
    ]

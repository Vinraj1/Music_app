# Generated by Django 5.2 on 2025-04-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music_app', '0002_rename_audio_files_song_audio_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

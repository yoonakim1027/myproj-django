# Generated by Django 3.2.9 on 2022-01-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubemusic', '0005_auto_20220113_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='photo',
            new_name='album_photo',
        ),
        migrations.AddField(
            model_name='music',
            name='singer_photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]

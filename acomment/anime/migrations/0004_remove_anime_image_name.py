# Generated by Django 5.0 on 2024-06-02 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0003_alter_anime_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='image_name',
        ),
    ]

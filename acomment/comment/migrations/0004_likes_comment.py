# Generated by Django 5.0 on 2024-06-04 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='comment',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='comment.comment'),
        ),
    ]

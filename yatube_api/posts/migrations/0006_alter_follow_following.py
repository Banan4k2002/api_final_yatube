# Generated by Django 3.2.16 on 2024-04-03 19:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_auto_20240403_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='following',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='followings',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Подпись',
            ),
        ),
    ]

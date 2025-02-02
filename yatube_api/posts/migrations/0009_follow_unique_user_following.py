# Generated by Django 3.2.16 on 2024-04-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_follow_unique_together'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(
                fields=('user', 'following'), name='unique_user_following'
            ),
        ),
    ]

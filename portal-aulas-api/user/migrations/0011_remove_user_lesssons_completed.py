# Generated by Django 4.0.10 on 2023-05-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_user_lesssons_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lesssons_completed',
        ),
    ]

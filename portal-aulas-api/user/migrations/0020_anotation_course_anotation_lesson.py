# Generated by Django 4.0.10 on 2023-06-19 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_ratings_user_name'),
        ('lessons', '0007_alter_lesson_users_who_completed'),
        ('user', '0019_remove_anotation_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotation',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AddField(
            model_name='anotation',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson'),
        ),
    ]

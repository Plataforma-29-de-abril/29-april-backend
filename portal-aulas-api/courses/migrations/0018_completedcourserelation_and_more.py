# Generated by Django 4.0.10 on 2023-06-17 02:06

import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0017_alter_ratings_course_alter_ratings_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedCourseRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.FileField(upload_to=courses.models.get_certificate_path)),
                ('date', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.AddConstraint(
            model_name='completedcourserelation',
            constraint=models.UniqueConstraint(fields=('course', 'student'), name='unique_course_student_certificate'),
        ),
    ]

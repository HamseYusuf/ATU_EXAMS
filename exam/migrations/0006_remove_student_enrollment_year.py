# Generated by Django 5.1 on 2024-08-16 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_alter_semester_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrollment_year',
        ),
    ]

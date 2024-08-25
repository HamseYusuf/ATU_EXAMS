# Generated by Django 5.1 on 2024-08-16 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_alter_semester_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='enrollment_year',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exam.faculty'),
            preserve_default=False,
        ),
    ]

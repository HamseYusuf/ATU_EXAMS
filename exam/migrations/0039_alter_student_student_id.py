# Generated by Django 5.1 on 2024-08-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0038_remove_examresult_grade_point_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

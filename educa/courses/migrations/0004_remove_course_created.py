# Generated by Django 3.0 on 2020-10-31 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='created',
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-01 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0004_auto_20240801_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reformstatus',
            name='notes',
        ),
    ]
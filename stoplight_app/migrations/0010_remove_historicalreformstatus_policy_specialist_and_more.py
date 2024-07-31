# Generated by Django 5.0.7 on 2024-07-31 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0009_add_citation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reformstatus',
            name='version',
        ),
        migrations.AlterField(
            model_name='reform',
            name='version',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Version 1'), (2, 'Version 2')], default=1),
        ),
    ]

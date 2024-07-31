# Generated by Django 5.0.7 on 2024-07-31 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0010_remove_historicalreformstatus_policy_specialist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reform',
            name='version',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Version 1'), (2, 'Version 2')], default=2),
        ),
    ]

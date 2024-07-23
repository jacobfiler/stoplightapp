# Generated by Django 5.0.7 on 2024-07-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0007_reform_last_updated_reformstatus_win_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalreformstatus',
            name='last_updated',
            field=models.DateTimeField(blank=True, default='2023-01-01 00:00:00', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reform',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
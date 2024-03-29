# Generated by Django 5.0.1 on 2024-02-06 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reformstatus',
            name='reform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoplight_app.reform'),
        ),
        migrations.AlterField(
            model_name='reformstatus',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stoplight_app.state'),
        ),
        migrations.AlterField(
            model_name='reformstatus',
            name='status',
            field=models.CharField(blank=True, choices=[('R', 'Red'), ('Y', 'Yellow'), ('G', 'Green'), ('N', 'Null')], default='N', max_length=1, null=True),
        ),
    ]

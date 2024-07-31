from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0006_remove_historicalreformstatus_policy_specialist_and_more'),  # Update with your latest migration
    ]

    operations = [
        migrations.AlterField(
            model_name='reformstatus',
            name='version',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='reformstatus',
            name='citation',
            field=models.TextField(blank=True, null=True),
        ),
    ]

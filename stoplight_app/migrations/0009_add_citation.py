from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0008_remove_historicalreformstatus_policy_specialist_and_more'),  # Update with your latest migration
    ]

    operations = [
        migrations.AddField(
            model_name='reformstatus',
            name='citation',
            field=models.TextField(blank=True, null=True),
        ),
    ]

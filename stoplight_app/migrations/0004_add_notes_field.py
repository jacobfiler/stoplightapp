from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('stoplight_app', '0003_remove_historicalreformstatus_policy_specialist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reformstatus',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reformstatus',
            name='version',
            field=models.IntegerField(default=2),
        ),
    ]

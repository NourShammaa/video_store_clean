from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_add_release_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration_minutes',
            field=models.PositiveIntegerField('Duration (min)', null=True, blank=True),
        ),
    ]

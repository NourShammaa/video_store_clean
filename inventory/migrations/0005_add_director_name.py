from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_add_actor_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='director_name',
            field=models.CharField('DirectorName', max_length=120, default=''),
            preserve_default=False,
        ),
    ]

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_add_movie_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='actor1_name',
            field=models.CharField('Actor1Name', max_length=120, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='actor2_name',
            field=models.CharField('Actor2Name', max_length=120, blank=True, default=''),
            preserve_default=False,
        ),
    ]

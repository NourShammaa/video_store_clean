from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial_movie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='movie_title',
            field=models.CharField('MovieTitle', max_length=200, default='Untitled'),
            preserve_default=False,
        ),
    ]

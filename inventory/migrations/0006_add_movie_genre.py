from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_add_director_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='movie_genre',
            field=models.CharField('MovieGenre', max_length=20, default='OTHER'),
            preserve_default=False,
        ),
    ]

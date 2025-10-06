from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_add_movie_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='movie_description',
            field=models.TextField('Description', blank=True, default=''),
            preserve_default=False,
        ),
    ]

from django.db import migrations, models
import django.core.validators

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_add_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='release_year',
            field=models.PositiveIntegerField(
                'ReleaseYear',
                validators=[
                    django.core.validators.MinValueValidator(1888),
                    django.core.validators.MaxValueValidator(2100),
                ],
                default=2000,
            ),
            preserve_default=False,
        ),
    ]

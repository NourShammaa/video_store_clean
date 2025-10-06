from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GENRE_CHOICES = [
    ("COMEDY","Comedy"),("ROMANCE","Romance"),("ACTION","Action"),("DRAMA","Drama"),
    ("HORROR","Horror"),("SCIFI","Sci-Fi"),("ANIMATION","Animation"),("THRILLER","Thriller"),("OTHER","Other"),
]

class Video(models.Model):
    movie_id = models.CharField("MovieID", max_length=20, unique=True)
    movie_title = models.CharField("MovieTitle", max_length=200)
    movie_description = models.TextField("Description", blank=True)
    actor1_name = models.CharField("Actor1Name", max_length=120)
    actor2_name = models.CharField("Actor2Name", max_length=120, blank=True)
    director_name = models.CharField("DirectorName", max_length=120)
    movie_genre = models.CharField("MovieGenre", max_length=20, choices=GENRE_CHOICES, default="OTHER")  # <-- keep this
    release_year = models.PositiveIntegerField(
        "ReleaseYear", validators=[MinValueValidator(1888), MaxValueValidator(2100)]
    )
    duration_minutes = models.PositiveIntegerField("Duration (min)", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["movie_title"]

    def __str__(self):
        return f"{self.movie_title} ({self.release_year})"

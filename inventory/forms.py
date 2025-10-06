from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            "movie_id","movie_title","movie_description",
            "actor1_name","actor2_name","director_name",
            "movie_genre","release_year","duration_minutes",
        ]
        labels = {
            "movie_id":"MovieID 🆔",
            "movie_title":"Movie Title 🎞️",
            "movie_description":"Description 📝",
            "actor1_name":"Actor 1 🎭",
            "actor2_name":"Actor 2 🎭",
            "director_name":"Director 🎬",
            "movie_genre":"Genre 🗂️",
            "release_year":"Release Year 📅",
            "duration_minutes":"Duration ⏱️ (min)",
        }
        widgets = {
            "movie_id": forms.TextInput(attrs={"class":"form-control","placeholder":"MV-0001"}),
            "movie_title": forms.TextInput(attrs={"class":"form-control","placeholder":"e.g., West Beirut"}),
            "movie_description": forms.Textarea(attrs={"class":"form-control","rows":4,"placeholder":"Short plot or notes…"}),
            "actor1_name": forms.TextInput(attrs={"class":"form-control","placeholder":"Lead actor"}),
            "actor2_name": forms.TextInput(attrs={"class":"form-control","placeholder":"Supporting (optional)"}),
            "director_name": forms.TextInput(attrs={"class":"form-control","placeholder":"e.g., Ziad Doueiri"}),
            "movie_genre": forms.Select(attrs={"class":"form-select"}),
            "release_year": forms.NumberInput(attrs={"class":"form-control","min":1888,"max":2100,"placeholder":"1998"}),
            "duration_minutes": forms.NumberInput(attrs={"class":"form-control","min":1,"placeholder":"100"}),
        }

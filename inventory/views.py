from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Video
from .forms import VideoForm


class VideoListView(ListView):
    model = Video
    template_name = "inventory/video_list.html"
    context_object_name = "videos"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(movie_title__icontains=q) |
                Q(movie_id__icontains=q) |
                Q(actor1_name__icontains=q) |
                Q(actor2_name__icontains=q) |
                Q(director_name__icontains=q) |
                Q(movie_genre__icontains=q)
            )
        return qs

class VideoDetailView(DetailView):
    model = Video
    template_name = "inventory/video_detail.html"
    context_object_name = "video"

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = "inventory/video_form.html"
    success_url = reverse_lazy("inventory:video-list")

class VideoUpdateView(UpdateView):
    model = Video
    form_class = VideoForm
    template_name = "inventory/video_form.html"
    success_url = reverse_lazy("inventory:video-list")

class VideoDeleteView(DeleteView):
    model = Video
    template_name = "inventory/video_confirm_delete.html"
    success_url = reverse_lazy("inventory:video-list")

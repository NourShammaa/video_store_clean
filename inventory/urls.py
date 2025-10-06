from django.urls import path
from .views import VideoListView, VideoDetailView, VideoCreateView, VideoUpdateView, VideoDeleteView
app_name = "inventory"
urlpatterns = [
    path('', VideoListView.as_view(), name='video-list'),
    path('add/', VideoCreateView.as_view(), name='video-add'),
    path('<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('<int:pk>/edit/', VideoUpdateView.as_view(), name='video-edit'),
    path('<int:pk>/delete/', VideoDeleteView.as_view(), name='video-delete'),
]

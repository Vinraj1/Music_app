from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.urls import path,include

app_name = "Music_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload-song/", views.upload_song, name="upload_song"),
    path('search/', views.search, name='search'),
    path('get-video/', views.get_video_api, name='get_video_api'),
]
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.urls import path,include

app_name = "Music_app"

urlpatterns = [
    path("", views.index, name="index"),
]
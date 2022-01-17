from django.urls import path, include
from rest_framework.routers import DefaultRouter
from youtubemusic import views

app_name = "youtubemusic"

router = DefaultRouter()
router.register("music", views.MusicViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

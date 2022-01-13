from django.urls import path, include
from rest_framework.routers import DefaultRouter

from typinggame import views

app_name = "typing"

router = DefaultRouter()
router.register("typing", views.TypingViewSet)

urlpatterns = [
    # path("articles.json", views.article_list),
    path("api/", include(router.urls)),
]
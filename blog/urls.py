from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet

app_name = 'blog'

#앱마다 한번씩 만드는 것
router = DefaultRouter()
router.register("posts", PostViewSet)
urlpatterns = [
    path("api/", include(router.urls)),

]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog import views
from blog.views import PostViewSet

app_name = 'blog'

# 앱마다 한번씩 만드는 것
router = DefaultRouter()
router.register("posts", PostViewSet)
urlpatterns = [
    # path("blogs.json", views.post_list),
    path("api/", include(router.urls)),

]

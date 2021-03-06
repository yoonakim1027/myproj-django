from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.views import review_list, review_new, ReviewViewSet


app_name = "shop"

router = DefaultRouter()
router.register("reviews", ReviewViewSet)

urlpatterns = [
    path("reviews/", review_list, name="review_list"),
    path("reviews/new/", review_new, name="review_new"),
    path("api/", include(router.urls)),
]

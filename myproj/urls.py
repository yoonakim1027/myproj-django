from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="root.html"), name="root"),  # 빈 문자열이 최상위 주소를 뜻함
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
    path("blog/", include("blog.urls")),
    path("news/", include("news.urls")),
    path("youtubemusic/", include("youtubemusic.urls")),
    path("accounts/", include("accounts.urls")),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

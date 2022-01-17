# 아래 token view는 accounts앱 내에 두는 것이 맞습니다! 곧 옮길 것
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = "accounts"

urlpatterns = []

# 토큰을 발급받는 주소가 바뀌게 됨
urlpatterns += [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]



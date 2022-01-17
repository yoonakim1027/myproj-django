from rest_framework_simplejwt.views import (
    TokenObtainPairView as OrigTokenObtainPairView,
    TokenRefreshView as OrigTokenRefreshView,
)
from accounts.serializers import TokenObtainPairSerializer


# 여기서만 응답을 바꿀 것 -> urls 에서는 여기서 지정된 애들을 쓰게 되는 것

class TokenObtainPairView(OrigTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    # 이렇게 지정을 하면 ? serializer_class를 바꾸게 된것


class TokenRefreshView(OrigTokenRefreshView):
    pass

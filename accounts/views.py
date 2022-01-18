from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView as OrigTokenObtainPairView,
    TokenRefreshView as OrigTokenRefreshView,
)
from accounts.serializers import TokenObtainPairSerializer, UserCreationSerializer
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# 여기서만 응답을 바꿀 것 -> urls 에서는 여기서 지정된 애들을 쓰게 되는 것

# 항상 모든 API는 쿼리셋을 받아야함
User = get_user_model()  # 제일 정석적인 방법


# 직접 auth에서 get_user_model을 import 하는 것이 정석!
class SignupAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer
    permission_classes = [AllowAny]  # 지금 프로젝트의 default permission 은 allow
    # queryset, serializer_class 가 꼭 필수인 두 항목
    # 이렇게 세개가 기본 뷰 구현


class TokenObtainPairView(OrigTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    # 이렇게 지정을 하면 ? serializer_class 를 바꾸게 된것


class TokenRefreshView(OrigTokenRefreshView):
    pass

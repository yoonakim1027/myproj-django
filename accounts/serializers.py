from typing import Dict

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
    # 두개가 부모.
)


class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):

    # 다끝나고 나서 응답을 만들 때쓰는 것이 user
    @classmethod
    def get_token(cls, user) -> Dict:  # typing의 Dict -> 이렇게 타입을 명시해야 ~ 덜 헷갈릴것
        token = super().get_token(user)  # 부모를 호출해서 그 반환값을 token(사전)으로 받음
        token['username'] = user.username
        token['first_name']= user.first_name
        token['last_name']= user.last_name
        return token

# 내가 추가하고 싶은 값이 있으면? 그 토큰에서 추가
# 새로운 토큰을 발급 받을 때, 기존 토큰이 영향을 받지 않는다

class TokenRefreshSerializer(OrigTokenRefreshSerializer):
    pass

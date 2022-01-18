from typing import Dict

from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
    # 두개가 부모.
)

# serializers의 유효성 검사는 validate
class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):
    # access/ refresh 속성 외에 추가 속성 !
    def validate(self, attrs):
        data = super().validate(attrs)
        # 밑의 세개의 속성값을 추가하는 것
        data['username'] = self.user.username
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
    #TODO : 프로필 이미지 URL
        return data


# 아래의 코드는 JWT Payload 커스텀
# 다끝나고 나서 응답을 만들 때쓰는 것이 user
# 이것들 정도 말고 더 많은 것을 추가하면 ~ 안돼 ~
# @classmethod
# def get_token(cls, user) -> Dict:  # typing의 Dict -> 이렇게 타입을 명시해야 ~ 덜 헷갈릴것
#     token = super().get_token(user)  # 부모를 호출해서 그 반환값을 token(사전)으로 받음
#     token['username'] = user.username
#     token['first_name'] = user.first_name
#     token['last_name'] = user.last_name
#     return token


# 내가 추가하고 싶은 값이 있으면? 그 토큰에서 추가
# 새로운 토큰을 발급 받을 때, 기존 토큰이 영향을 받지 않는다

class TokenRefreshSerializer(OrigTokenRefreshSerializer):
    pass

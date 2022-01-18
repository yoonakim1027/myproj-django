from typing import Dict

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
    # 두개가 부모.
)

User = get_user_model()


class UserCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])  # 필수여부 지정 = required=True
    password2 = serializers.CharField(write_only=True, required=True)  # 필수여부 지정 = required=True

    # write_only = True -> DB에 저장만 -> 조회할 때 응답으로는 패스워드 응답은 안주겠다.
    # 유저모델과 관련된 시리얼모델
    class Meta:
        model = User
        fields = ["username", "password", "password2"]



    # 모든 유효성 검사도 가져오는 것

    # 위에서 받은 password, password2가 같은 지 유효성 검사가 필요
    # 두 개 이상의 필드에 대해 유효성 검사를 할 때 validate를 사용
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("동일한 암호를 지정해주세요.")
        return attrs

    # 생성할 때에는? serializers에서는 구분되어있음
    def create(self, validated_data):
        # 뭘 리턴하냐면? 생성된 User 모델 인스턴스
        username = validated_data['username']
        password = validated_data['password']
        # password2는 접근할 필요 없음. 위에서 유효성 검사만 끝나면 볼일이 없어서~


        new_user = User(username=username) # 새 유저 생성
        new_user.set_password(password) # 새 유저의 비밀번호 설정
        new_user.save() # 저장
        return new_user # 유저 정보를 리턴


# validate -> 조건에 맞지 않을 때~
# serializers의 유효성 검사는 validate
# form 에서는 cleaned_data로 접근 가능

class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):
    # access/ refresh 속성 외에 추가 속성 !
    def validate(self, attrs):
        data = super().validate(attrs)
        # 밑의 세개의 속성값을 추가하는 것
        data['username'] = self.user.username
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name
        # TODO : 프로필 이미지 URL
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

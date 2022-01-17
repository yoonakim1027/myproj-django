from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as OrigTokenObtainPairSerializer,
    TokenRefreshSerializer as OrigTokenRefreshSerializer,
# 두개가 부모.
)

class TokenObtainPairSerializer(OrigTokenObtainPairSerializer):
    pass

class TokenRefreshSerializer(OrigTokenRefreshSerializer):
    pass





from rest_framework import serializers
from blog.models import Post


# DRF의 serializers 사용
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"  # 실제 서비스에서는 모든 필드가 노출되는 __all__는 비추
        # serializer는 데이터베이스에 대한 유효성 검사, 디비 저장을 함

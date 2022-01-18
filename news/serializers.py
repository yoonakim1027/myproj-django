from django.contrib.auth import get_user_model
from rest_framework import serializers
import re
from news.models import Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name"]


class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "photo", "author"]
        # 그러면 이 네 가지 항목만 유효성검사를 하게 된다!
        # 실제 서비스에서는 "__all__" X!!

    # # 여기서 하는 것 보다 model에 validator를 정의 하는 것이 좋다
    # def validate_title(self, title):
    #     if len(title) < 3:
    #         raise serializers.ValidationError("3글자 이상!!")
    #     if not re.search(r"[ㄱ-힣]", title):  # ㄱ-힣 한글이 들어갈 수 있는 범위
    #         raise serializers.ValidationError("한글을 써주세요!!")
    #     return title
    #

# 차별화를 둬서 각각 권한마다 보여지는 것을 다르게!
# # 비로그인 사용자용
# class ArticleAnonymousSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content"]
#
#
# # 골드멤버쉽 사용자용
# class ArticleGoldMembershipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content", "photo"]
#
#
# # 관리자용
# class ArticleAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ["id", "title", "content", "photo", "created_at", "updated_at"]

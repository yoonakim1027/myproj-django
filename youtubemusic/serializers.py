import re
from rest_framework import serializers
from youtubemusic.models import Music


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"


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

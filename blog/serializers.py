from rest_framework import serializers
from blog.models import Post


# DRF의 serializers 사용
from django.contrib.auth import get_user_model
from rest_framework import serializers
import re
from news.models import Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name"]


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "photo", "author"]
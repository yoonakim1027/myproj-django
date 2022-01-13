import json
from django.db import models
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Article(TimestampedModel):
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(blank=True)  # 옵션 형태


# django에서 이미지를 쓰려면 pillow 가 필수!


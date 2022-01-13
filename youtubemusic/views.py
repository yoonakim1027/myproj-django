import json

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from youtubemusic.models import Music

from rest_framework.generics import ListAPIView
# from news.serializers import ArticleAnonymousSerializer, ArticleAdminSerializer, ArticleGoldMembershipSerializer
from youtubemusic.serializers import MusicSerializer


class MusicViewSet(ModelViewSet):

    queryset = Music.objects.all()  # 설정의 영역
    serializer_class = MusicSerializer



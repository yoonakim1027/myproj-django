import json

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from youtubemusic.models import Music

from rest_framework.generics import ListAPIView
# from news.serializers import ArticleAnonymousSerializer, ArticleAdminSerializer, ArticleGoldMembershipSerializer
from youtubemusic.serializers import MusicSerializer


class MusicViewSet(ModelViewSet):

    queryset = Music.objects.all()  # 설정의 영역
    #serializer_class = MusicSerializer

    def get_serializer_class(self):
        return MusicSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query","")
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

import json

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from typinggame.models import Typing
from rest_framework.generics import ListAPIView

# from news.serializers import ArticleAnonymousSerializer, ArticleAdminSerializer, ArticleGoldMembershipSerializer
from typinggame.serializers import TypingSerializer


class TypingViewSet(ModelViewSet):
    queryset = Typing.objects.all()  # 설정의 영역

    # serializer_class = ArticleSerializer

    def get_serializer_class(self):
        return TypingSerializer

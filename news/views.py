import json

from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from news.models import Article
from news.serializers import ArticleSerializer
from rest_framework.generics import ListAPIView
# from news.serializers import ArticleAnonymousSerializer, ArticleAdminSerializer, ArticleGoldMembershipSerializer


class ArticleViewSet(ModelViewSet):
    # 한번 고정! 바뀌지 않는 고정부분
    # 클래스 부분 변수 : 클래스 변수는 클래스가 정의될 때 한번 셋팅 (정적인 셋팅)
    queryset = Article.objects.all()  # 설정의 영역
    # serializer_class = ArticleSerializer


    def get_serializer_class(self):
        return ArticleSerializer

    #     # 보여지는 데이터를 결정하는 것은 view가 아니라
    #     # serializer임!
    #     # 데이터의 응답을 결정하는 것이 serializer !
    #     # form 보다 기능이 하나 더 있음
    #     # 조건문에 따라서? AnonymousSerializer이냐 ~ gold냐 ~결정 가능

    # # get_ 함수를 통해서 동적인 처리를 가능하게 한다
    # # instance 함수 정의 ->  이렇게 함수를 통해 클래스를 변화
    # def get_queryset(self):
    #     # 조회할 때 사용되는 쿼리셋을 만드는 용도
    #     qs = super().get_queryset()
    #     query = self.request.query_params.get("query", "")  # query가 있으면 가져오고 없으면 빈문자열
    #     if query:
    #         qs = qs.filter(title_icontains=query)
    #     year = self.request.query_params.get("year", "")
    #     if year:
    #         qs = qs.filter(created_at__year=year)
    #         # 각각 지원되는 __데이터 타입이 다르다~
    #     return qs

# article_list = ListAPIView.as_view(
#     queryset=Article.objects.all(),
#     serializer_class=ArticleSerializer,
# )
# #
# qs = Article.objects.all()
#
# # step 2
# serializer = ArticleSerializer(qs, many=True)
# data = serializer.data
# # data = [
# #     {
# #         "id": article.id,
# #         "title": article.title,  # 파이썬의 문자열
# #         "content": article.content,  # 파이썬의 문자열로 읽어올 수 있음
# #         "photo": request.build_absolute_uri(article.photo.url) if article.photo else None,  # 앞의 값이 참이면 앞에 것, 뒤에것이 참이면 뒤엣것
# #         # 포토 필드는 파일을 읽어오는 것.
# #         # 우리가 응답으로 줘야할 것은 ? url 을 응답으로 줘야 한다
# #
# #     }
# #     for article in qs
# # ]
# json_string = json.dumps(data)
# return HttpResponse(json_string)

from rest_framework.viewsets import ModelViewSet
from news.models import Article
from news.serializers import ArticleSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
# IsAuthenticated : 유저가 누군지는 상관없고, 인증만 되면 이 API를 호출
# from news.serializers import ArticleAnonymousSerializer, ArticleAdminSerializer, ArticleGoldMembershipSerializer


# list, detail, create, update, delete를 1개 ViewSet에서 지원

class ArticleViewSet(ModelViewSet):
    # 한번 고정! 바뀌지 않는 고정부분
    # 클래스 부분 변수 : 클래스 변수는 클래스가 정의될 때 한번 셋팅 (정적인 셋팅)
    queryset = Article.objects.all()  # 설정의 영역
    serializer_class = ArticleSerializer

    def get_permissions(self): #여기가 함수 정의부
        # 항상 django 내에서의 method비교는 대문자!!

        if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
            return [IsAuthenticated()]
        return [AllowAny()]
    #permission_classes = [IsAuthenticated]


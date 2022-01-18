from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from news.models import Article
from news.serializers import ArticleSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


# IsAuthenticated : 유저가 누군지는 상관없고, 인증만 되면 이 API를 호출
# from news.serializers import ArticleAnonymousSerializer, ArticleAdminSerializer, ArticleGoldMembershipSerializer


# list, detail, create, update, delete를 1개 ViewSet에서 지원
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [AllowAny]  # DRF 디폴트 설정
    # permission_classes = [IsAuthenticated]
    # 위 주석 한줄과 아래는 같은 결과

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):
        if self.request.method == "GET":
            # 각각을 언제 쓰느냐를 잘 봐
            return [AllowAny()]
        return [IsAuthenticated()]

    # 유효성 검사가 끝나고 나서
    # 실제  serializer.save()를 할 때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않음
        # 대신 키워드 인자를 통한 속성 지정을 지원함
        serializer.save(author=self.request.user)
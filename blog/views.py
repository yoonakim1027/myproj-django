import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
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


#
# def post_list(request):
#     qs = Post.objects.all()
#     data = [
#         {
#             "id": post.id,
#             "title": post.title,
#             "content": post.content,
#         }
#         for post in qs
#     ] #리스트 컴프리헨션
#     json_string = json.dumps(data)
#     return HttpResponse(json_string)

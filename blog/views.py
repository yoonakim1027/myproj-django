import json

from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from blog.models import Post
from blog.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    # serializer_class = PostSerializer

    def get_serializer_class(self):
        return PostSerializer


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

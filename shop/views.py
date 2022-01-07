from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from shop.form import ReviewForm
from shop.models import Review
from shop.serializers import ReviewSerializer

# list, detail, create 등 모든 구현들이 이 안에 다 구현되어 있음

# 장고의 뷰 -> 요청이 오면 실제 실행을 하는 함수
review_list = ListView.as_view(model=Review)
review_new = CreateView.as_view(
    model=Review,
    form_class=ReviewForm,
    success_url=reverse_lazy("shop:review_list"))


# 유효성 검사를 해주는 주체가 form
# success_url로 저장되면 이동한다!


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
# 어던 모델에 대해서? 어떤 시리얼라이저로 처리할 것인지만 정하면 됨

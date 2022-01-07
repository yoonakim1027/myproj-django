from rest_framework import serializers
from shop.models import Review


# drf 에서 API 유효성검사 하려고 할 시에
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

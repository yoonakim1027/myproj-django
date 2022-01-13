import re
from rest_framework import serializers
from typinggame.models import Typing


class TypingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typing
        fields = "__all__"


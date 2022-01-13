from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Typing(models.Model):
    name = models.CharField(max_length=100, db_index=True,
                            validators=[
                                MinLengthValidator(3, message="최소 3글자 이상 입력해주세요."),
                                RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
                            ])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

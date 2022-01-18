from django.conf import settings
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=100,
        db_index=True,
        validators=[
            MinLengthValidator(3, message="최소 3글자 이상 입력해주세요."),
            RegexValidator(r"[ㄱ-힣]", message="한글을 입력해주세요."),
        ],
    )
    content = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

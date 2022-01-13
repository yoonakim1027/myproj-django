import json
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.validators import MaxValueValidator
from django.db import models
from django.http import HttpResponse


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    title = models.CharField(max_length=200, db_index=True, unique=True,
                             validators=[
                                 MinLengthValidator(3, message="최소 3글자 이상 입력해주세요! "),
                                 RegexValidator(r"[ㄱ-힣]",message="한글을 입력해주세요."),
                             ])
    content = models.TextField()
    photo = models.ImageField(blank=True)



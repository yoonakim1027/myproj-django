from django.core.validators import MinLengthValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Music(TimestampedModel):
    title = models.CharField(max_length=100, db_index=True,
                             validators=[
                                 MinLengthValidator(1, message="최소 한 글자 이상 입력해주세요.")
                             ])
    singer = models.TextField()
    content = models.TextField()
    photo = models.ImageField()

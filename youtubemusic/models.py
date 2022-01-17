from django.core.validators import MinLengthValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Music(TimestampedModel):
    title = models.CharField(
        max_length=100,
        db_index=True,
        validators=[MinLengthValidator(1, message="최소 한 글자 이상 입력해주세요.")],
    )
    singer = models.TextField()
    content = models.TextField()
    album_photo = models.ImageField()
    singer_photo = models.ImageField()
    mood = models.CharField(
        max_length=7,
        choices=[
            ("hiphop", "힙할 때"),
            ("sad", "우울할 때"),
            ("fun", "신났을 때"),
            ("run", "운동할 때"),
            ("groove", "분위기 좋은 와인바에서"),
            ("study", "집중할 때"),
        ],
        default="hiphop",
    )

    class Meta:
        ordering = ["-id"]  # 정렬은 여러 개를 지정할 수 있다.

        verbose_name = "음악"  # 단수
        verbose_name_plural = "음악 목록"  # 복수


class User(TimestampedModel):

    name = models.CharField(
        max_length=100,
        db_index=True,
        validators=[MinLengthValidator(1, message="최소 한 글자 이상 입력해주세요")],
    )
    choice_mood = models.CharField(
        max_length=7,
        choices=[
            ("hiphop", "힙할 때"),
            ("sad", "우울할 때"),
            ("fun", "신났을 때"),
            ("run", "운동할 때"),
            ("groove", "분위기 좋은 와인바에서"),
            ("study", "집중할 때"),
        ],
        default="hiphop",
    )

    class Meta:
        ordering = ["-id"]

        verbose_name = "사용자"  # 단수
        verbose_name_plural = "사용자 목록"  # 복수

from django import forms
from shop.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:  # 옵션지정
        model = Review
        fields = "__all__"



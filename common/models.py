from django.db import models


class CommonModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstact: True  # 추상화 시킬 것. DB에 테이블을 추가하지 않겠다.

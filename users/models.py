from django.db import models
from django.contrib.auth.models import AbstractUser

# username: 유저 이름
# profileIntroduce: 유저 소개글
# profileImg: 유저 프로필 사진
# followerNum: 유저 팔로워 수


class User(AbstractUser):
    profileImg = models.URLField(blank=True)
    profileIntroduce = models.CharField(max_length=150)
    followerNum = models.PositiveIntegerField(default=0)

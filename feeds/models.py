from django.db import models
from common.models import CommonModel


# caption: 게시글 내용
# contentImg: 게시글 이미지
# likesNum: 좋아요 갯수
# reviewsNum: 댓글 갯수

# USER - foreign key
class Feed(CommonModel):
    caption = models.CharField(max_length=1000, default="")  # 게시글 내용
    contentImg = models.URLField(blank=True)  # 게시글 이미지
    likesNum = models.PositiveIntegerField(default=0)  # 좋아요 갯수
    reviewsNum = models.PositiveIntegerField(default=0)  # 리뷰 갯수

    # 1:N (User:Feed), N이 ForeignKey 가진다.
    # User는 여러 개의 Reiview를 작성할 수 있다.a
    # Feed는 여러 개의 Review를 가질 수 있다.
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,  # user가 삭제되면 게시글도 사라짐
        related_name="feeds"
        # (users.feed_set.all() = users.feeds.all())
    )

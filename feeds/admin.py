from django.contrib import admin
from feeds.models import Feed


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = (
        "caption",
        "likesNum",
        "reviewsNum",
    )

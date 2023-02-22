from django.urls import path

# views.py에서 AllFeeds 불러오기
from .views import AllFeeds

urlpatterns = [

    # http://127.0.0.1:8000/api/v1/feeds/
    path("", AllFeeds.as_view())

]

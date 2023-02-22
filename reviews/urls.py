from django.urls import path

# views.py에서 AllReviews 불러오기
from .views import AllReviews

urlpatterns = [

    # http://127.0.0.1:8000/api/v1/reviews/
    path("", AllReviews.as_view())

]

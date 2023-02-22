from django.urls import path

# views.py에서 MyInfo를 불러오기
from .views import MyInfo

urlpatterns = [

    # http://127.0.0.1:8000/api/v1/users/myinfo
    path("myinfo", MyInfo.as_view())

]

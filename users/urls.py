from django.urls import path

# views.py에서 MyInfo를 불러오기
from .views import MyInfo

urlpatterns = [

    path("myinfo", MyInfo.as_view())

]

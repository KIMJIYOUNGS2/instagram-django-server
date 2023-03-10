from django.shortcuts import render

from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class MyInfo(APIView):
    # 로그인한 유저만 MyInfo 호출을 허용하겠다
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 장고만 이해할 수 있는 형태이니까
        user = request.user

        # Serialize화 해줘야 user에게 보낼 수 있음
        serializer = UserSerializer(user)

        return Response(serializer.data)

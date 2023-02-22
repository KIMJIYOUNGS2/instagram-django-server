from django.shortcuts import render

from .serializers import ReviewSerializer

# orm
from .models import Review

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class AllReviews(APIView):
    # 로그인한 유저만 AllReviews 호출을 허용하겠다
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 장고만 이해할 수 있는 형태이니까 Serialize화 해줘야 user에게 보낼 수 있음
        # Review모델의 모든 객체
        all_reviews = Review.objects.all()

        # many=True 설정해줘야 함
        serializer = ReviewSerializer(all_reviews, many=True)

        return Response(serializer.data)

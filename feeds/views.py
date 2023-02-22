from django.shortcuts import render

from .serializers import FeedSerializer

# orm
from .models import Feed

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class AllFeeds(APIView):
    # 로그인한 유저만 AllFeeds 호출을 허용하겠다
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 장고만 이해할 수 있는 형태이니까 Serialize화 해줘야 user에게 보낼 수 있음
        # Feed모델의 모든 객체
        all_feeds = Feed.objects.all()

        # many=True 설정해줘야 함
        serializer = FeedSerializer(all_feeds, many=True)

        return Response(serializer.data)

from .models import Users
from .serializers import BSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class ListView(APIView):
    def get(self, request):
        u_qset = Users.objects.all()
        serializer = BSerializer(u_qset,many=True)
        return Response({'members' : list(serializer.data)},status=status.HTTP_201_CREATED)
        
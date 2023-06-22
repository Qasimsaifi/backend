from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import User
from .serializers import UserSerializer

class UserDetailView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            data = {
                'id': user.id,
                'email': user.email,
                'mobile': user.mobile,
                'profile_picture': user.profile_picture.url if user.profile_picture else None,
                'name': {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'full_name': user.first_name + " " + user.last_name
                }
            }
            return Response(data)
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)


    def delete(self, request):
        user = request.user
        if user.is_authenticated:
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)

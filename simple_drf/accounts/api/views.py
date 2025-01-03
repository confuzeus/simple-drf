from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from simple_drf.accounts.api.serializers import UserDeleteSerializer, UserSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(instance=request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(
            data=request.data, instance=request.user, partial=True
        )
        if serializer.is_valid():
            instance = serializer.save()
            serializer = UserSerializer(instance)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, request):
        serializer = UserDeleteSerializer(
            data=request.data, context={"user": request.user}
        )
        if serializer.is_valid():
            serializer.destroy()
            request.session.flush()
            return Response(status=status.HTTP_410_GONE)
        return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

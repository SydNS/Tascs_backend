from django.contrib.auth import authenticate
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from .Serializers import TaskSerialiser, UserSerializer
from .models import Tasks, TascsUAccount


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = Tasks.objects.all()
    serializer_class = TaskSerialiser

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied(
                request.user.username + " You can not create a Tasc, you haven't logged in")
        return super().create(request, *args, **kwargs)


class UserCreate(viewsets.ModelViewSet):
    authentication_classes = ()
    permission_classes = ()
    queryset = TascsUAccount.objects.order_by('-id')
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()

    def post(self, request, ):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key, "username": user.username})
            # return Response({"token": "logged in"})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

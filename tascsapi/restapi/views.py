from rest_framework import viewsets

from .Serializers import TaskSerialiser
from .models import Tasks


class TaskViewSet(viewsets.ModelViewSet):


    queryset = Tasks.objects.all()
    serializer_class = TaskSerialiser
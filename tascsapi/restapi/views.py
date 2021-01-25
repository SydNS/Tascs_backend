from rest_framework import viewsets

from tascsapi.restapi.Serializers import TaskSerialiser
from tascsapi.restapi.models import Tasks


class NoteViewSet(viewsets.ModelViewSet):

    queryset = Tasks.objects.all()
    serializer_class = TaskSerialiser
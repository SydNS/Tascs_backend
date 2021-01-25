from rest_framework import serializers
from .models import Tasks


class TaskSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'created_at', 'created_by', 'priority')

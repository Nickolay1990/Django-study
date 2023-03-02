from lesson_9.models import ModelForLesson9
from rest_framework import serializers


class SerializerForTask1(serializers.ModelSerializer):
    class Meta:
        model = ModelForLesson9
        fields = ['name']

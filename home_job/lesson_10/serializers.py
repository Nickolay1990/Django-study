from rest_framework import serializers
from lesson_10.models import GamesBase, Cityes


class GamesBaseSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = GamesBase
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cityes
        fields = '__all__'

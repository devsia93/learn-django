from rest_framework import serializers
from mysite.models import *
from django.contrib.auth import get_user_model


class TopingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Toping
        fields = ('id', 'slug', 'title', 'content')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username')


class PizzaSerializer(serializers.ModelSerializer):
    topings = TopingSerializer(many=True, read_only=True)
    cook = UserSerializer(read_only=True)

    class Meta:
        model = Pizza
        fields = ('id', 'slug', 'title', 'content', 'topings', 'cook')

from rest_framework import serializers
from .models import Superhero


class SuperheroSerializer(serializers.ModelSerializer):
    members = serializers.JSONField()

    class Meta:
        model = Superhero
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    members = serializers.JSONField()

    class Meta:
        model = Superhero
        fields = ('members',)






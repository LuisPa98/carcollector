from rest_framework import serializers
from .models import Shoe, Worn, Shoelace
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

class ShoelaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoelace
        fields = '__all__'

class ShoeSerializer(serializers.ModelSerializer):
    shoelace = ShoelaceSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Shoe
        fields = '__all__'


class WornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worn
        fields = '__all__'
        read_only_fields = ('shoe')


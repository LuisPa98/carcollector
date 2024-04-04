from rest_framework import serializers
from .models import Shoe, Worn, Shoelace

class ShoelaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoelace
        fields = '__all__'

class ShoeSerializer(serializers.ModelSerializer):
    shoelace = ShoelaceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Shoe
        fields = '__all__'


class WornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worn
        fields = '__all__'
        read_only_fields = ('shoe')


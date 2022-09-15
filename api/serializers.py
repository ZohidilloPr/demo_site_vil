# import serializer from rest_framework
from rest_framework import serializers
from main.models import Bitiruvchi

class BitiruvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bitiruvchi
        fields = '__all__'
        depth = 1
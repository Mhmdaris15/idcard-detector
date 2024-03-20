# serializers.py
from rest_framework import serializers
from .models import CustomUser, IDCard, IDCardMatch

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class IDCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDCard
        fields = '__all__'

class IDCardMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDCardMatch
        fields = '__all__'

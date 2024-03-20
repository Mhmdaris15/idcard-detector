from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, IDCard, IDCardMatch
from .serializers import CustomUserSerializer, IDCardSerializer, IDCardMatchSerializer

# Create your views here.

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class IDCardViewSet(viewsets.ModelViewSet):
    queryset = IDCard.objects.all()
    serializer_class = IDCardSerializer

class IDCardMatchViewSet(viewsets.ModelViewSet):
    queryset = IDCardMatch.objects.all()
    serializer_class = IDCardMatchSerializer

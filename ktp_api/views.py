from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser, IDCard, IDCardMatch
from .serializers import CustomUserSerializer, IDCardSerializer, IDCardMatchSerializer
import requests
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def fetch_data(request, id):  
    if request.method == 'POST':
        url = settings.PUBLIC_API_ENDPOINT
        
        try:
            response = requests.post(url, headers={
                'X-RapidAPI-Key': settings.API_KEY,
                'X-RapidAPI-Host': settings.API_HOST,
            }, json={
                'nik': id  
            })
            data = response.json()
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
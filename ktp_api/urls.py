# urls.py
from rest_framework import routers
from .views import CustomUserViewSet, IDCardViewSet, IDCardMatchViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'idcards', IDCardViewSet)
router.register(r'idcardmatches', IDCardMatchViewSet)

urlpatterns = [
    path('fetch-data/<str:id>/', views.fetch_data, name='fetch_data'),
] + router.urls

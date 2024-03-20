# urls.py
from rest_framework import routers
from .views import CustomUserViewSet, IDCardViewSet, IDCardMatchViewSet

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)
router.register(r'idcards', IDCardViewSet)
router.register(r'idcardmatches', IDCardMatchViewSet)

urlpatterns = [
    # Your other URL patterns
] + router.urls

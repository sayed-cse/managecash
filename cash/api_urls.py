from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CashViewSet

router = DefaultRouter()
router.register(
    "cash",
    CashViewSet,
    basename="cash"
)

urlpatterns = [
    path("",include(router.urls)),
]
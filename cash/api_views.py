from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Cash
from .serializers import CashSerializer

class CashViewSet(viewsets.ModelViewSet):

    serializer_class = CashSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cash.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
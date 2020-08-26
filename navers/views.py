from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Naver
from .serializers import (
    NaverSerializer,
    NaverCreateSerializer,
    NaverDetailSerializer
)


class NaverViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'admission_date', 'job_role']

    def get_queryset(self):
        return Naver.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        action_list = ['create', 'update', 'partial_update']

        if hasattr(self, 'action') and self.action in action_list:
            return NaverCreateSerializer

        if hasattr(self, 'action') and self.action == 'retrieve':
            return NaverDetailSerializer

        return NaverSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

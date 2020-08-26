from rest_framework import viewsets
from django_filters import rest_framework as filters

from .models import Naver
from .serializers import (
    NaverSerializer,
    NaverCreateSerializer,
    NaverDetailSerializer
)


class NaverFilter(filters.FilterSet):
    admission_date_gte = filters.DateFilter(field_name="admission_date", lookup_expr='gte')
    admission_date_lte = filters.DateFilter(field_name="admission_date", lookup_expr='lte')

    class Meta:
        model = Naver
        fields = ['name', 'job_role', 'admission_date_gte', 'admission_date_lte']


class NaverViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = NaverFilter

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

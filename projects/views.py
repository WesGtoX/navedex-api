from rest_framework import viewsets

from .models import Project
from .serializers import (
    ProjectSerializer,
    ProjectCreateSerializer,
    ProjectDetailSerializer
)


class ProjectViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Project.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        action_list = ['create', 'update', 'partial_update']

        if hasattr(self, 'action') and self.action in action_list:
            return ProjectCreateSerializer

        if hasattr(self, 'action') and self.action == 'retrieve':
            return ProjectDetailSerializer

        return ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

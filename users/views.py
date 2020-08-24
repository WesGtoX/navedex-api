from .models import User
from .serializers import UserSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

    def perform_create(self, serializer):
        super(UserViewSet, self).perform_create(serializer=serializer)

    def list(self, request, *args, **kwargs):
        return Response(dict(status=405), status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, *args, **kwargs):
        return Response(dict(status=405), status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response(dict(status=405), status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response(dict(status=405), status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response(dict(status=405), status=status.HTTP_405_METHOD_NOT_ALLOWED)

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from .views import redirect_view
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    path('api-auth/', include('rest_framework.urls')),

    path('', redirect_view),
]

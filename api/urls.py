from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from .views import redirect_view
from users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api-auth/', include('rest_framework.urls')),

    path('', redirect_view),
]

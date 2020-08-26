from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt import views as jwt_views

from . import routers
from .views import redirect_view

from users.views import UserViewSet

from navers import urls as naver_url
from projects import urls as project_url

router = routers.CustomRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/navers/store/', naver_url.naver_create, name='naver-create'),
    path('api/v1/navers/index/', naver_url.naver_list, name='naver-list'),
    path('api/v1/navers/show/<int:pk>/', naver_url.naver_detail, name='naver-detail'),
    path('api/v1/navers/update/<int:pk>/', naver_url.naver_update, name='naver-update'),
    path('api/v1/navers/delete/<int:pk>/', naver_url.naver_delete, name='naver-delete'),

    path('api/v1/projects/store/', project_url.project_create, name='project-create'),
    path('api/v1/projects/index/', project_url.project_list, name='project-list'),
    path('api/v1/projects/show/<int:pk>/', project_url.project_detail, name='project-detail'),
    path('api/v1/projects/update/<int:pk>/', project_url.project_update, name='project-update'),
    path('api/v1/projects/delete/<int:pk>/', project_url.project_delete, name='project-delete'),

    path('api-auth/', include('rest_framework.urls')),

    path('', redirect_view),
]

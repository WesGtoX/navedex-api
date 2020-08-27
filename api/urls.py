from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

from . import routers
from users.views import UserViewSet

from navers import urls as naver_url
from projects import urls as project_url

router = routers.CustomRouter()
router.register(r'signup', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('navers/store/', naver_url.naver_create, name='naver-create'),
    path('navers/index/', naver_url.naver_list, name='naver-list'),
    path('navers/show/<int:pk>/', naver_url.naver_detail, name='naver-detail'),
    path('navers/update/<int:pk>/', naver_url.naver_update, name='naver-update'),
    path('navers/delete/<int:pk>/', naver_url.naver_delete, name='naver-delete'),

    path('projects/store/', project_url.project_create, name='project-create'),
    path('projects/index/', project_url.project_list, name='project-list'),
    path('projects/show/<int:pk>/', project_url.project_detail, name='project-detail'),
    path('projects/update/<int:pk>/', project_url.project_update, name='project-update'),
    path('projects/delete/<int:pk>/', project_url.project_delete, name='project-delete'),

    path('api-auth/', include('rest_framework.urls')),
]


admin.site.site_header = "Navedex API Administration"
admin.site.site_title = 'Navedex API Admin'
admin.site.index_title = "Navedex API Admin"

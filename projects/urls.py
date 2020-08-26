from .views import ProjectViewSet


project_create = ProjectViewSet.as_view({
    'post': 'create'
})
project_list = ProjectViewSet.as_view({
    'get': 'list',
})
project_detail = ProjectViewSet.as_view({
    'get': 'retrieve',
})
project_update = ProjectViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
})
project_delete = ProjectViewSet.as_view({
    'delete': 'destroy'
})

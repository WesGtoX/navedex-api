from navers.views import NaverViewSet


naver_create = NaverViewSet.as_view({
    'post': 'create'
})
naver_list = NaverViewSet.as_view({
    'get': 'list',
})
naver_detail = NaverViewSet.as_view({
    'get': 'retrieve',
})
naver_update = NaverViewSet.as_view({
    'put': 'update',
    'patch': 'partial_update',
})
naver_delete = NaverViewSet.as_view({
    'delete': 'destroy'
})

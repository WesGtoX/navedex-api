from collections import OrderedDict
from rest_framework import routers


class CustomRouter(routers.DefaultRouter):

    def get_api_root_view(self, api_urls=None):
        api_root_dict = OrderedDict()
        list_name = self.routes[0].name
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)

        api_root_dict['navers-store'] = 'naver-create'
        api_root_dict['navers-index'] = 'naver-list'
        api_root_dict['navers-show'] = 'naver-detail'
        api_root_dict['navers-update'] = 'naver-update'
        api_root_dict['navers-delete'] = 'naver-delete'

        api_root_dict['projects-store'] = 'project-create'
        api_root_dict['projects-index'] = 'project-list'
        api_root_dict['projects-show'] = 'project-detail'
        api_root_dict['projects-update'] = 'project-update'
        api_root_dict['projects-delete'] = 'project-delete'

        return self.APIRootView.as_view(api_root_dict=api_root_dict)

from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

perm_paths = paths['perm']


class Perm(InterfaceBase):

    def perm_get_agent(self, host, param):
        url = host + version + perm_paths['perm_get_queryset_sql']
        return self.Post(url, param)

    def perm_check_conditions(self, host, param):
        url = host + version + perm_paths['perm_validate_conditions']
        return self.Post(url, param)

    def perm_validate_resource_scope(self, host, param):
        url = host + version + perm_paths['perm_validate_resource_scope']
        return self.Post(url, param)

    def perm_validate_cross_join(self, host, param):
        url = host + version + perm_paths['perm_validate_cross_join']
        return self.Post(url, param)

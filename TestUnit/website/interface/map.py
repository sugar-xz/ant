from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

map_paths = paths['map']


class Map(InterfaceBase):

    def map_config_list(self, host, param=None):
        url = host + version + map_paths['map_map_config']
        return self.Get(url, params=param)

    def map_create_config(self, host, param):
        url = host + version + map_paths['map_map_config']
        return self.Post(url, param)

    def map_retrieve_config(self, host, map_config_id):
        url = host + version + map_paths['map_map_config'] + '/' + str(map_config_id)
        return self.Get(url)

    def map_delete_config(self, host, map_config_id):
        url = host + version + map_paths['map_map_config'] + '/' + str(map_config_id)
        return self.Delete(url)

    def map_map_list(self, host, param=None):
        url = host + version + map_paths['map_map']
        return self.Get(url, params=param)

    def map_create_map(self, host, param):
        url = host + version + map_paths['map_map']
        return self.Post(url, param)

    def map_retrieve_map(self, host, map_id):
        url = host + version + map_paths['map_map'] + '/' + str(map_id)
        return self.Get(url)

    def map_delete_map(self, host, map_id):
        url = host + version + map_paths['map_map'] + '/' + str(map_id)
        return self.Delete(url)

    def map_target_list(self, host, param=None):
        url = host + version + map_paths['map_target']
        return self.Get(url, params=param)

    def map_create_target(self, host, param):
        url = host + version + map_paths['map_target']
        return self.Post(url, param)

    def map_retrieve_target(self, host, map_target_id):
        url = host + version + map_paths['map_target'] + '/' + str(map_target_id)
        return self.Get(url)

    def map_delete_target(self, host, map_target_id):
        url = host + version + map_paths['map_target'] + '/' + str(map_target_id)
        return self.Delete(url)

    def map_site_add_map(self, host, site_id, param):
        url = host + version + map_paths['map_site'] + site_id + '/add_map'
        return self.Post(url, param)

    def map_site_remove_map(self, host, site_id, param):
        url = host + version + map_paths['map_site'] + site_id + '/remove_map'
        return self.Post(url, param)

    def map_domain_set_map(self, host, domain_id, param):
        url = host + version + map_paths['map_domain'] + domain_id + '/set_map'
        return self.Post(url, param)

    def map_domain_unset_map(self, host, domain_id, param):
        url = host + version + map_paths['map_domain'] + domain_id + '/unset_map'
        return self.Post(url, param)

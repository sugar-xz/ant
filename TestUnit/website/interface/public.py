from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

public_paths = paths['public']


class Public(InterfaceBase):

    def public_get_agent(self, host, param):
        """
        :param host:
        :param param: {'name':'pc_v1'}
        :return:
        """
        url = host + version + public_paths['public_get_agent']
        return self.Get(url, params=param)

    def public_get_global(self, host, param=None):
        url = host + version + public_paths['public_get_global']
        return self.Get(url, params=param)

    def public_get_timezones(self, host, param=None):
        url = host + version + public_paths['public_get_timezones']
        return self.Get(url, params=param)

    def public_all_event_types(self, host, param=None):
        url = host + version + public_paths['public_all_event_types']
        return self.Get(url, params=param)

    def public_cleanup_task_list(self, host, param=None):
        url = host + version + public_paths['public_manual_cleanup_task']
        return self.Get(url, params=param)

    def public_create_cleanup_task(self, host, param):
        url = host + version + public_paths['public_manual_cleanup_task']
        return self.Post(url, param)

    def public_retrieve_cleanup_task(self, host, task_id, param=None):
        url = host + version + public_paths['public_manual_cleanup_task'] + '/' + str(task_id)
        return self.Get(url, params=param)

from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

ccs_paths = paths['ccs']


class Ccs(InterfaceBase):

    def ccs_sample_list(self, host, param=None):
        url = host + version + ccs_paths['ccs_sample']
        return self.Get(url, params=param)

    def ccs_retrieve_sample(self, host, sample_id, param=None):
        url = host + version + ccs_paths['ccs_sample'] + '/' + str(sample_id)
        return self.Get(url, params=param)

    def ccs_update_sample(self, host, sample_id, param):
        url = host + version + ccs_paths['ccs_sample'] + '/' + str(sample_id)
        return self.Put(url, param)

    def ccs_update_part_sample(self, host, sample_id, param):
        url = host + version + ccs_paths['ccs_sample'] + '/' + str(sample_id)
        return self.Patch(url, param)

    def ccs_raw_event_list(self, host, param=None):
        url = host + version + ccs_paths['ccs_raw_event']
        return self.Get(url, params=param)

    def ccs_retrieve_raw_event(self, host, raw_event_id, param=None):
        url = host + version + ccs_paths['ccs_raw_event'] + '/' + str(raw_event_id)
        return self.Get(url, params=param)

    def ccs_raw_event_misreport(self, host, raw_event_id, param):
        url = host + version + ccs_paths['ccs_raw_event'] + '/' + str(raw_event_id) + '/misreport'
        return self.Put(url, param)

    def ccs_raw_event_verified(self, host, raw_event_id, param):
        url = host + version + ccs_paths['ccs_raw_event'] + '/' + str(raw_event_id) + '/verified'
        return self.Put(url, param)

    #   Only box
    def ccs_box_create_raw_event(self, host, param):
        url = host + version + ccs_paths['ccs_raw_event'] + '/create_or_update_for_camera'
        return self.Post(url, param)

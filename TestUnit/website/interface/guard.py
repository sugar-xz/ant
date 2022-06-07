from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

guard_paths = paths['guard']


class Guard(InterfaceBase):

    def guard_company_list(self, host):
        url = host + version + guard_paths['guard_company']
        return self.Get(url)

    def guard_create_guard_company(self, host, param):
        url = host + version + guard_paths['guard_company']
        return self.Post(url, param)

    def guard_retrieve_guard_company(self, host, guard_company_id, param=None):
        url = host + version + guard_paths['guard_company'] + str(guard_company_id)
        return self.Get(url, params=param)

    def guard_update_guard_company(self, host, guard_company_id, param):
        url = host + version + guard_paths['guard_company'] + str(guard_company_id)
        return self.Put(url, param)

    def guard_delete_guard_company(self, host, guard_company_id):
        url = host + version + guard_paths['guard_company'] + str(guard_company_id)
        return self.Delete(url)

    def guard_admin_list(self, host):
        url = host + version + guard_paths['guard_admin']
        return self.Get(url)

    def guard_create_guard_admin(self, host, param):
        url = host + version + guard_paths['guard_admin']
        return self.Post(url, param)

    def guard_retrieve_guard_admin(self, host, guard_admin_id, param=None):
        url = host + version + guard_paths['guard_admin'] + str(guard_admin_id)
        return self.Get(url, params=param)

    def guard_update_guard_admin(self, host, guard_admin_id, param):
        url = host + version + guard_paths['guard_admin'] + str(guard_admin_id)
        return self.Put(url, param)

    def guard_delete_guard_admin(self, host, guard_admin_id):
        url = host + version + guard_paths['guard_admin'] + str(guard_admin_id)
        return self.Delete(url)

    def guard_list(self, host):
        url = host + version + guard_paths['guard_guard']
        return self.Get(url)

    def guard_create_guard(self, host, param):
        url = host + version + guard_paths['guard_guard']
        return self.Post(url, param)

    def guard_retrieve_guard(self, host, guard_id, param=None):
        url = host + version + guard_paths['guard_guard'] + str(guard_id)
        return self.Get(url, params=param)

    def guard_update_guard(self, host, guard_id, param):
        url = host + version + guard_paths['guard_guard'] + str(guard_id)
        return self.Put(url, param)

    def guard_delete_guard(self, host, guard_id):
        url = host + version + guard_paths['guard_guard'] + str(guard_id)
        return self.Delete(url)

    def guard_guard_resend_activate_email(self, host, param):
        url = host + version + guard_paths['guard_guard'] + '/resend_activate_email'
        return self.Post(url, param)

    def guard_monitoring_operator_list(self, host):
        url = host + version + guard_paths['monitoring_operator']
        return self.Get(url)

    def guard_create_monitoring_operator(self, host, param):
        url = host + version + guard_paths['monitoring_operator']
        return self.Post(url, param)

    def guard_retrieve_monitoring_operator(self, host, guard_id, param=None):
        url = host + version + guard_paths['monitoring_operator'] + str(guard_id)
        return self.Get(url, params=param)

    def guard_update_monitoring_operator(self, host, guard_id, param):
        url = host + version + guard_paths['monitoring_operator'] + str(guard_id)
        return self.Put(url, param)

    def guard_delete_monitoring_operator(self, host, guard_id):
        url = host + version + guard_paths['monitoring_operator'] + str(guard_id)
        return self.Delete(url)

    def guard_monitoring_operator_resend_activate_email(self, host, param):
        url = host + version + guard_paths['monitoring_operator'] + '/resend_activate_email'
        return self.Post(url, param)

    def guard_case_list(self, host, param=None):
        url = host + version + guard_paths['guard_new_case']
        return self.Get(url, params=param)

    def guard_update_guard_case(self, host, guard_case_id, param):
        url = host + version + guard_paths['guard_new_case'] + str(guard_case_id)
        return self.Post(url, param)

    def guard_update_part_guard_case(self, host, guard_case_id, param):
        url = host + version + guard_paths['guard_new_case'] + str(guard_case_id)
        return self.Put(url, param)

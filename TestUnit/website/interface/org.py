from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

org_paths = paths['org']


class Org(InterfaceBase):

    def org_organization_list(self, host, param=None):
        url = host + version + org_paths['org_organization']
        return self.Get(url, params=param)

    def org_retrieve_organization(self, host, org_id):
        url = host + version + org_paths['org_organization'] + '/' + str(org_id)
        return self.Get(url)

    def org_update_organization(self, host, org_id, param):
        url = host + version + org_paths['org_organization'] + '/' + str(org_id)
        return self.Put(url, param)

    def org_domain_type_list(self, host, param=None):
        url = host + version + org_paths['org_domain_type']
        return self.Get(url, params=param)

    def org_create_domain_type(self, host, param):
        url = host + version + org_paths['org_domain_type']
        return self.Post(url, param)

    def org_retrieve_domain_type(self, host, domain_type_id):
        url = host + version + org_paths['org_domain_type'] + '/' + str(domain_type_id)
        return self.Get(url)

    def org_update_domain_type(self, host, domain_type_id, param):
        url = host + version + org_paths['org_domain_type'] + '/' + str(domain_type_id)
        return self.Put(url, param)

    def org_update_part_domain_type(self, host, domain_type_id, param):
        url = host + version + org_paths['org_domain_type'] + '/' + str(domain_type_id)
        return self.Patch(url, param)

    def org_delete_domain_type(self, host, domain_type_id):
        url = host + version + org_paths['org_domain_type'] + '/' + str(domain_type_id)
        return self.Delete(url)

    def org_domain_list(self, host, param=None):
        url = host + version + org_paths['org_domain']
        return self.Get(url, params=param)

    def org_create_domain(self, host, param):
        url = host + version + org_paths['org_domain']
        return self.Post(url, param)

    def org_retrieve_domain(self, host, domain_id):
        url = host + version + org_paths['org_domain'] + '/' + str(domain_id)
        return self.Get(url)

    def org_update_domain(self, host, domain_id, param):
        url = host + version + org_paths['org_domain'] + '/' + str(domain_id)
        return self.Put(url, param)

    def org_update_part_domain(self, host, domain_id, param):
        url = host + version + org_paths['org_domain'] + '/' + str(domain_id)
        return self.Patch(url, param)

    def org_delete_domain(self, host, domain_id):
        url = host + version + org_paths['org_domain'] + '/' + str(domain_id)
        return self.Delete(url)

    def org_create_domain_user(self, host, domain_id, param):
        url = host + version + org_paths['org_domain'] + '/' + str(domain_id) + '/attach_user'
        return self.Post(url, param)

    def org_associate_domain_map(self, host, domain_id, param):
        url = host + version + org_paths['org_domain'] + '/' + str(domain_id) + '/set_map'
        return self.Post(url, param)

    def org_unassociate_domain_map(self, host, domain_id, param):
        url = host + version + org_paths['org_domain'] + '/' + str(domain_id) + '/unset_map'
        return self.Post(url, param)

    def org_user_node_list(self, host):
        url = host + version + org_paths['org_user_node']
        return self.Get(url)

    def org_retrieve_user_node(self, host, user_node_id):
        url = host + version + org_paths['org_user_node'] + '/' + str(user_node_id)
        return self.Get(url)

    def org_create_user_role(self, host, param):
        url = host + version + org_paths['org_user_node'] + '/create_user_roles'
        return self.Post(url, param)

    def org_update_user_node(self, host, user_node_id, param):
        url = host + version + org_paths['org_user_node'] + '/' + str(user_node_id) + '/edit_user_roles'
        return self.Post(url, param)

    def org_remove_user_node(self, host, user_node_id, param):
        url = host + version + org_paths['org_user_node'] + '/' + str(user_node_id) + '/remove_user'
        return self.Post(url, param)

    def org_change_user_node_parent(self, host, user_node_id, param):
        url = host + version + org_paths['org_user_node'] + '/' + str(user_node_id) + '/change_parent'
        return self.Post(url, param)

    def org_retrieve_org_validate(self, host, param):
        url = host + version + org_paths['org_retrieve_org_validate']
        return self.Post(url, param)

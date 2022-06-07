from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

org_paths = paths['user']


class User(InterfaceBase):

    def user_login(self, host, param):
        url = host + org_paths['user_login_jwt']
        return self.Post(url, param)

    def user_login_cookie(self, host, param):
        url = host + version + org_paths['user_login_cookie']
        return self.Post(url, param)

    def user_view_me(self, host):
        url = host + version + org_paths['user_view_me']
        return self.Get(url)

    def user_update_info(self, host, user_id, param):
        url = host + version + org_paths['user_update_info'] + str(user_id)
        return self.Put(url, param)

    def user_change_password(self, host, param):
        url = host + version + org_paths['user_change_password']
        return self.Post(url, param)

    def user_reset_password(self, host, param):
        url = host + version + org_paths['user_reset_password']
        return self.Post(url, param)

    def user_register(self, host, param):
        url = host + version + org_paths['user_register_user']
        return self.Post(url, param)

    def user_register_android(self, host, param):
        url = host + version + org_paths['user_register_android']
        return self.Post(url, param)

    def user_register_ios(self, host, param):
        url = host + version + org_paths['user_register_ios']
        return self.Post(url, param)



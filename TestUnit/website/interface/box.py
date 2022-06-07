from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

box_paths = paths['box']


class Box(InterfaceBase):

    def box_view_list(self, host, param=None):
        url = host + version + box_paths['box_box']
        return self.Get(url, params=param)

    def box_retrieve_a_box(self, host, box_id):
        url = host + version + box_paths['box_box'] + '/' + str(box_id)
        return self.Get(url)

    def box_initiate(self, host, param):
        url = host + version + box_paths['box_box'] + '/initiate'
        return self.Post(url, param)

    def box_initiate_auth(self, host, param):
        url = host + version + box_paths['box_initiate_auth']
        return self.Post(url, param)

    def box_authenticate(self, host, param):
        url = host + version + box_paths['box_box'] + '/authenticate'
        return self.Post(url, param)

    def box_authenticate_auth(self, host, param):
        url = host + version + box_paths['box_authenticate_auth']
        return self.Post(url, param)

    def box_debug_login(self, host, param):
        url = host + version + box_paths['box_box'] + '/debug_login'
        return self.Post(url, param)

    def box_claim(self, host, param):
        url = host + version + box_paths['box_box'] + '/claim'
        return self.Post(url, param)

    def box_unclaim(self, host, param):
        url = host + version + box_paths['box_box'] + '/unclaim'
        return self.Post(url, param)

    def box_get_token(self, host, param=None):
        url = host + version + box_paths['box_box'] + '/get_token'
        if param is None:
            name_list = ['camera_preview', 'camera_events', 'camera_snaps', 'camera_videos']
            import random
            name = {'name': random.choice(name_list)}
            return self.Get(url, name)
        else:
            return self.Get(url, params=param)

    def box_get_config(self, host):
        url = host + version + box_paths['box_box'] + '/get_config'
        return self.Get(url)

    def box_different(self, host, param):
        url = host + version + box_paths['box_box'] + '/different'
        return self.Post(url, param)

    def box_get_meta(self, host, box_id):
        url = host + version + box_paths['box_box'] + '/' + str(box_id) + '/get_meta'
        return self.Get(url)

    #   Only box use
    def box_get_stream_token(self, host, param):
        """
        :param host:
        :param param: {"camera_id": 1}
        :return:
        """
        url = host + version + box_paths['box_box'] + '/get_stream_token'
        return self.Get(url, params=param)

    #   Only box use
    def box_update_state(self, host, param):
        url = host + version + box_paths['box_box'] + '/update_state'
        return self.Post(url, param)

    def box_create_update_camera(self, host, param):
        url = host + version + box_paths['box_box'] + '/create_or_update_cameras'
        return self.Post(url, param)

    def camera_view_all(self, host, param=None):
        """
        :param host:
        :param param: {'ids':'1,2', 'box_id': 'box_test_10001'}
        :return:
        """
        url = host + version + box_paths['camera_camera']
        return self.Get(url, params=param)

    def camera_user_create_camera(self, host, param):
        url = host + version + box_paths['camera_camera']
        return self.Post(url, param)

    def camera_retrieve(self, host, camera_id):
        url = host + version + box_paths['camera_camera'] + '/' + str(camera_id)
        return self.Get(url)

    def camera_update(self, host, camera_id, param):
        url = host + version + box_paths['camera_camera'] + '/' + str(camera_id)
        return self.Put(url, param)

    def camera_delete(self, host, camera_id):
        url = host + version + box_paths['camera_camera'] + '/' + str(camera_id)
        return self.Delete(url)

    def camera_differences(self, host, param):
        url = host + version + box_paths['camera_camera'] + '/differences'
        return self.Post(url, param)

    def camera_video_correlation_list(self, host, param=None):
        """
        :param host:
        :param param: {'camera_id': 1}
        :return:
        """
        url = host + version + box_paths['camera_video_correlation']
        return self.Get(url, params=param)

    def camera_video_correlation_create(self, host, param):
        url = host + version + box_paths['camera_video_correlation']
        return self.Post(url, param)

    #   Only box use
    def camera_box_save_video(self, host, param):
        url = host + version + box_paths['camera_camera'] + '/saving_video'
        return self.Post(url, param)

    def camera_auto_update(self, host, param):
        url = host + version + box_paths['camera_camera'] + '/auto_update'
        return self.Post(url, param)

    def camera_videos_list(self, host, param=None):
        """
        :param host:
        :param param: {'camera_id':1,'started_at__gte':'', 'started_at__le':''}
        :return:
        """
        url = host + version + box_paths['camera_video']
        return self.Get(url, params=param)

    def camera_create_video(self, host, param):
        url = host + version + box_paths['camera_video']
        return self.Post(url, param)

    def camera_video_slot(self, host, param=None):
        """
        :param host:
        :param param: {'camera_id':1,'started_at__gte':'', 'started_at__le':''}
        :return:
        """
        url = host + version + box_paths['camera_video'] + '/slot'
        return self.Get(url, params=param)

    def camera_save_video(self, host, param):
        url = host + version + box_paths['camera_video'] + '/save_video'
        return self.Post(url, param)

    #   Only box use
    def camera_create_snap(self, host, param):
        url = host + version + box_paths['camera_snap']
        return self.Post(url, param)

    def camera_snap_slot(self, host, param=None):
        """
        :param host:
        :param param: {'camera_id':1,'started_at__gte':'', 'started_at__le':''}
        :return:
        """
        url = host + version + box_paths['camera_snap'] + '/slot'
        return self.Get(url, params=param)

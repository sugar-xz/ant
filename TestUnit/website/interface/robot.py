from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

robot_paths = paths['robot']


class Robot(InterfaceBase):

    def robot_initiate(self, host, param):
        url = host + version + robot_paths['robot_robot'] + '/initiate'
        return self.Post(url, param)

    def robot_initiate_auth(self, host, param):
        url = host + robot_paths['robot_initiate_auth']
        return self.Post(url, param)

    def robot_authenticate(self, host, param):
        url = host + version + robot_paths['robot_robot'] + '/authenticate'
        return self.Post(url, param)

    def robot_authenticate_auth(self, host, param):
        url = host + robot_paths['robot_authenticate_auth']
        return self.Post(url, param)

    def robot_debug_login(self, host, param):
        url = host + version + robot_paths['robot_robot'] + '/debug_login'
        return self.Post(url, param)

    #   Only robot use
    def robot_get_token(self, host, param=None):
        """
        :param host:
        :param param: {'name': ''}
        :return:
        """
        url = host + version + robot_paths['robot_robot'] + '/get_token'
        if param is None:
            name_list = ['robot_events', 'robot_snaps', 'robot_videos', 'robot_inspections']
            import random
            name = {'name': random.choice(name_list)}
            return self.Get(url, name)
        else:
            return self.Get(url, params=param)

    def robot_get_config(self, host):
        url = host + version + robot_paths['robot_robot'] + '/get_config'
        return self.Get(url)

    #   Only robot use
    def robot_get_stream_token(self, host, param):
        """
        :param host:
        :param param: {"camera_name": "front"}
        :return:
        """
        url = host + version + robot_paths['robot_robot'] + '/get_stream_token'
        return self.Get(url, params=param)

    #   Only robot use
    def robot_get_analytics_token(self, host, param=None):
        """
        :param host:
        :param param: {"name": ""}
        :return:
        """
        url = host + version + robot_paths['robot_robot'] + '/get_analytics_token'
        if param is None:
            name_list = ['robot_logs', 'robot_lidar']
            import random
            name = {'name': random.choice(name_list)}
            return self.Get(url, name)
        else:
            return self.Get(url, params=param)

    #   Only robot use
    def robot_update_state(self, host, param):
        """
        :param host:
        :param param: Use `partial` = false if failed last time
        :return:
        """
        url = host + version + robot_paths['robot_robot'] + '/update_state'
        return self.Post(url, param)

    def robot_claim(self, host, param):
        url = host + version + robot_paths['robot_robot'] + '/claim'
        return self.Post(url, param)

    def robot_unclaim(self, host, param):
        url = host + version + robot_paths['robot_robot'] + '/unclaim'
        return self.Post(url, param)

    def robot_view_list(self, host, param=None):
        url = host + version + robot_paths['robot_robot']
        return self.Get(url, params=param)

    def robot_retrieve_robot(self, host, robot_id):
        url = host + version + robot_paths['robot_robot'] + '/' + str(robot_id)
        return self.Get(url)

    def robot_update_robot(self, host, robot_id, param):
        url = host + version + robot_paths['robot_robot'] + '/' + str(robot_id)
        return self.Put(url, param)

    def robot_get_meta(self, host, robot_id):
        url = host + version + robot_paths['robot_robot'] + '/' + str(robot_id) + '/get_meta'
        return self.Get(url)

    def robot_different(self, host, param):
        url = host + version + robot_paths['robot_robot'] + '/differences'
        return self.Post(url, param)

    #   Only robot use
    def robot_update_robot_meta(self, host, param):
        url = host + version + robot_paths['robot_robot'] + '/update_robot_meta'
        return self.Put(url, param)

    def robot_route_list(self, host, param=None):
        url = host + version + robot_paths['robot_routes']
        return self.Get(url, params=param)

    def robot_create_route(self, host, param):
        url = host + version + robot_paths['robot_routes']
        return self.Post(url, param)

    def robot_retrieve_route(self, host, route_id):
        url = host + version + robot_paths['robot_routes'] + '/' + str(route_id)
        return self.Get(url)

    def robot_create_patrol(self, host, robot_id, param):
        url = host + version + '/robot/' + str(robot_id) + '/patrols'
        return self.Post(url, param)

    def robot_snaps_list(self, host, param=None):
        url = host + version + robot_paths['robot_snaps']
        return self.Get(url, params=param)

    def robot_create_snap(self, host, param):
        url = host + version + robot_paths['robot_snaps']
        return self.Post(url, param)

    def robot_retrieve_snap(self, host, snap_id):
        url = host + version + robot_paths['robot_snaps'] + '/' + str(snap_id)
        return self.Get(url)

    def robot_snaps_slot(self, host, param=None):
        """
        :param host:
        :param param: {'robot_id':''.'camera':'robot_camera_name','timestamp__gt':'','timestamp__lte':'','limit':'','offset':''}
        :return:
        """
        url = host + version + robot_paths['robot_snaps'] + '/slot'
        return self.Get(url, params=param)

    def robot_videos_list(self, host, param=None):
        """
        :param host:
        :param param: {'robot_id':''.'camera':'robot_camera_name','timestamp__gt':'','timestamp__lte':'','limit':'','offset':''}
        :return:
        """
        url = host + version + robot_paths['robot_videos']
        return self.Get(url, params=param)

    def robot_create_video(self, host, param):
        url = host + version + robot_paths['robot_videos']
        return self.Post(url, param)

    def robot_save_video(self, host, param):
        url = host + version + robot_paths['robot_videos'] + '/save_video'
        return self.Post(url, param)

    def robot_video_slot(self, host, param=None):
        """
        :param host:
        :param param: {'robot_id':''.'camera':'robot_camera_name','timestamp__gt':'','timestamp__lte':'','limit':'','offset':''}
        :return:
        """
        url = host + version + robot_paths['robot_videos'] + '/slot'
        return self.Get(url, params=param)

    def robot_save_video_list(self, host, param=None):
        """
        :param host:
        :param param: {'robot_id':''.'camera':'robot_camera_name'}
        :return:
        """
        url = host + version + robot_paths['robot_robot_saved_videos']
        return self.Get(url, params=param)

    def robot_inspection_list(self, host, param=None):
        """
        :param host:
        :param param: {'robot':'robot_id'.'site':'site_id','target':'target_id','route_id':'','map_id':'','target__visible':false,'mediums__name':'','limit':'','offset':''}
        :return:
        """
        url = host + version + robot_paths['robot_inspection']
        return self.Get(url, params=param)

    def robot_retrieve_inspection(self, host, inspection_id):
        url = host + version + robot_paths['robot_inspection'] + '/' + str(inspection_id)
        return self.Get(url)

    def robot_retrieve_robot_config(self, host, robot_id):
        url = host + robot_paths['robot_config'] + str(robot_id)
        return self.Get(url)

    def robot_update_robot_config(self, host, robot_id, param):
        url = host + robot_paths['robot_config'] + str(robot_id)
        return self.Put(url, param)

    def robot_config_map_list(self, host, robot_id):
        url = host + robot_paths['robot_config'] + str(robot_id) + '/maps'
        return self.Get(url)

    def robot_config_routes_list(self, host, robot_id):
        url = host + robot_paths['robot_config'] + str(robot_id) + '/routes'
        return self.Get(url)

    def patrol_target_list(self, host, param=None):
        """
        :param host:
        :param param: {'site_id'：'','serial_no':'','floor':''}
        :return:
        """
        url = host + version + robot_paths['patrol_target']
        return self.Get(url, params=param)

    def patrol_create_target(self, host, param):
        url = host + version + robot_paths['patrol_target']
        return self.Post(url, param)

    def patrol_update_target(self, host, target_id, param):
        url = host + version + robot_paths['patrol_target'] + '/' + str(target_id)
        return self.Put(url, param)

    def patrol_category_list(self, host, param=None):
        """
        :param host:
        :param param: {'site_id':''}
        :return:
        """
        url = host + version + robot_paths['patrol_target'] + '/list_categories'
        return self.Get(url, params=param)

    def patrol_floor_list(self, host, param=None):
        """
        :param host:
        :param param: {'site_id':''}
        :return:
        """
        url = host + version + robot_paths['patrol_target'] + '/list_floors'
        return self.Get(url, params=param)

    def patrol_categories_floors_list(self, host, param=None):
        """
        :param host:
        :param param: {'site_id'：''}
        :return:
        """
        url = host + version + robot_paths['patrol_target'] + '/all'
        return self.Get(url, params=param)

    def patrol_algo_config_list(self, host, param=None):
        """
        :param host:
        :param param: {'target_id'：'','waypoint_action':'','enabled':false}
        :return:
        """
        url = host + version + robot_paths['patrol_algo_config']
        return self.Get(url, params=param)

    def patrol_create_algo_config(self, host, algoConfig_id, param):
        url = host + version + robot_paths['patrol_algo_config'] + '/' + str(algoConfig_id)
        return self.Patch(url, param)

    def patrol_delete_algo_config(self, host, algoConfig_id, param):
        url = host + version + robot_paths['patrol_algo_config'] + '/' + str(algoConfig_id)
        return self.Delete(url, param)

    def patrol_enable_algo_config(self, host, param):
        url = host + version + robot_paths['patrol_algo_config'] + '/enable'
        return self.Post(url, param)

    def patrol_disable_algo_config(self, host, param):
        url = host + version + robot_paths['patrol_algo_config'] + '/disable'
        return self.Post(url, param)

    def patrol_detection_task_list(self, host, param=None):
        """
        :param host:
        :param param: {'target_id'：'','review_status':'','inspection_id':''}
        :return:
        """
        url = host + version + robot_paths['patrol_detection_task']
        return self.Get(url, params=param)

    def patrol_batch_results(self, host, param):
        url = host + version + robot_paths['patrol_detection_task'] + '/batch_results'
        return self.Post(url, param)

    def patrol_update_detection_task_config(self, host, task_id, param):
        url = host + version + robot_paths['patrol_detection_task'] + '/' + str(task_id) + '/review'
        return self.Post(url, param)

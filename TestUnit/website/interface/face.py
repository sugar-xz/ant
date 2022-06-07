from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

face_paths = paths['face']


class Face(InterfaceBase):

    def face_lib_list(self, host, param=None):
        """
        :param host:
        :param param: {'organization':'org_id'}
        :return:
        """
        url = host + version + face_paths['face_libs']
        return self.Get(url, params=param)

    def face_create_face_lib(self, host, param):
        url = host + version + face_paths['face_libs']
        return self.Post(url, param)

    def face_retrieve_face_lib(self, host, face_lib_id):
        url = host + version + face_paths['face_libs'] + '/' + str(face_lib_id)
        return self.Get(url)

    def face_update_face_lib(self, host, face_lib_id, param):
        url = host + version + face_paths['face_libs'] + '/' + str(face_lib_id)
        return self.Put(url, param)

    def face_delete_face_lib(self, host, face_lib_id):
        url = host + version + face_paths['face_libs'] + '/' + str(face_lib_id)
        return self.Delete(url)

    def face_detection_list(self, host, param=None):
        """
        :param host:
        :param param: {'lib':'face_lib_id','lib__organization': 'org_id'}
        :return:
        """
        url = host + version + face_paths['face_face']
        return self.Get(url, params=param)

    def face_create_face_detection(self, host, param):
        url = host + version + face_paths['face_face']
        return self.Post(url, param)

    def face_retrieve_face_detection(self, host, face_detection_id):
        url = host + version + face_paths['face_face'] + '/' + str(face_detection_id)
        return self.Get(url)

    def face_delete_face_detection(self, host, face_detection_id):
        url = host + version + face_paths['face_face'] + '/' + str(face_detection_id)
        return self.Delete(url)

    def face_detection_track_object_list(self, host, param=None):
        """
        :param host:
        :param param: {'serial_no':'','organization': 'org_id','name': 'track_name'}
        :return:
        """
        url = host + version + face_paths['face_tracking_objects']
        return self.Get(url, params=param)

    def face_create_detection_track_object(self, host, param):
        url = host + version + face_paths['face_tracking_objects']
        return self.Post(url, param)

    def face_retrieve_detection_track_object(self, host, face_track_id):
        url = host + version + face_paths['face_tracking_objects'] + '/' + str(face_track_id)
        return self.Get(url)

    def face_delete_detection_track_object(self, host, face_track_id):
        url = host + version + face_paths['face_tracking_objects'] + '/' + str(face_track_id)
        return self.Delete(url)

    def face_detection_track_record_list(self, host, param=None):
        """
        :param host:
        :param param:
            {started_at__gt,started_at__gte,started_at__lt,started_at__lte,
                ended_at__gt,ended_at__gte,ended_at__lt,ended_at__lte}
            {'serial_no':'','organization_id': '','name': 'track_name','event_id':'','site_id':'',
                'camera_id':'','tracking_object':'tracking_object_id'}
        :return:
        """
        url = host + version + face_paths['face_tracking_records']
        return self.Get(url, params=param)

    def face_retrieve_detection_track_record(self, host, face_record_id):
        url = host + version + face_paths['face_tracking_records'] + '/' + str(face_record_id)
        return self.Get(url)

    def face_delete_detection_track_record(self, host, face_record_id):
        url = host + version + face_paths['face_tracking_records'] + '/' + str(face_record_id)
        return self.Delete(url)

    def face_view_temperature_detection_setting(self, host):
        url = host + version + face_paths['face_setting']
        return self.Get(url)

    def face_update_temperature_detection_setting(self, host, param):
        url = host + version + face_paths['face_setting']
        return self.Put(url, param)

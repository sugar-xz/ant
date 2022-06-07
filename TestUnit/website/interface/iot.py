from testframe.interface.interface_base import InterfaceBase
from TestUnit.website import paths, version

iot_paths = paths['iot']


class Iot(InterfaceBase):

    def iot_retrieve_box_agent(self, host, box_id):
        url = host + version + iot_paths['iot_box_agent'] + str(box_id)
        return self.Get(url)

    def iot_retrieve_robot_agent(self, host, robot_id):
        url = host + version + iot_paths['iot_robot_agent'] + str(robot_id)
        return self.Get(url)

    def iot_get_associated_device(self, host, param):
        url = host + version + iot_paths['iot_device'] + 'get_associated_device'
        return self.Post(url, param)

    def iot_get_min_and_latest_lr(self, host, param):
        url = host + version + iot_paths['iot_device'] + 'get_min_and_latest_lr'
        return self.Post(url, param)

import unittest
from TestUnit.superbox.unit import Unit
"""
测试条件：
* 环境搭建成功，可启动
* export AUTO_SUPERBOX_URL=http://192.168.2.146:8000
* export API_VERSION=v1
"""


class Superbox(unittest.TestCase, Unit):

    # def setUp(self):
    # def tearDown(self):
    def test_01_algorithm(self):
        self.algorithmsImport()
        self.apis.algorithmsList()

    def test_02_camera(self):
        id1 = self.cameraCreate()
        id2 = self.cameraCreate(camera_name='delete_camera')
        self.camerasList()
        self.apis.cameraRetrieve(id1)

        self.cameraUpdate(id1)
        self.cameraUpdatePart(id2)

        self.camerasMode(id1)
        self.apis.camerasGet_all()
        self.apis.camerasEnableSampling()
        self.apis.camerasDisableSampling()
        self.apis.camerasRestart_all()

        self.apis.camerasAlgorithmsList()

        self.apis.cameraDelete(id1)
        self.apis.cameraDelete(id2)

    def test_03_event(self):
        camera_id = self.cameraCreate(camera_name='nanjing')
        event_id = self.eventCreate(camera_id=camera_id)
        del_event = self.eventCreate(camera_id=camera_id)

        self.eventsList()
        self.apis.eventRetrieve(event_id)
        self.apis.eventsUnmarked()
        self.eventUpdate(event_id)
        self.eventRetrieve_ids()
        self.eventRetrieves()
        self.apis.eventDelete(del_event)
        self.apis.eventsDelete()
        self.apis.cameraDelete(camera_id)

    def test_04_medium(self):
        camera_id = self.cameraCreate(camera_name='nanjings')
        event_id = self.eventCreate(camera_id=camera_id)
        img_id = self.mediumCreate(event_id)
        video_id = self.mediumCreate(event_id, mediums_name='video')

        self.apis.mediumsList()
        self.apis.mediumRetrieve(img_id)
        self.apis.mediumRetrieve(video_id)
        self.mediumUpdate(video_id, mediums_name='bbox')
        self.mediumUpdatePart(img_id)
        self.mediumUpdatePart(video_id, mediums_name='video')

        self.apis.mediumDelete(img_id)
        self.apis.mediumDelete(video_id)

        self.apis.eventDelete(event_id)
        self.apis.cameraDelete(camera_id)

    def test_05_rule(self):
        camera_id = self.cameraCreate(camera_name='nanjings')
        rule_id = self.ruleCreate(camera_id)
        self.apis.rulesList()
        self.apis.ruleRetrieve(rule_id)
        self.ruleUpdatePart(rule_id)
        self.apis.ruleDelete(rule_id)

    def test_06_sample(self):
        camera_id = self.cameraCreate(camera_name='nanjings')
        sample_id = self.sampleCreate(camera_id=camera_id)
        self.apis.samplesList()
        self.apis.sampleRetrieve(sample_id)
        self.sampleUpdatePart(sample_id)
        self.apis.sampleDelete(sample_id)
        self.apis.cameraDelete(camera_id)

    def test_07_setting(self):
        setting_id = self.settingCreate()
        self.apis.settingsList()
        self.apis.settingRetrieve(setting_id)
        self.settingUpdatePart(setting_id)
        self.apis.settingDelete(setting_id)

        setting_id2 = self.settingCreate(value='test_case', name='test_case')
        self.settingItemList(name='test_case')
        self.settingItem()
        self.apis.settingDelete(setting_id2)


if __name__ == '__main__':
    unittest.main()

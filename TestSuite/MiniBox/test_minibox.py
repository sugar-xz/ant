import unittest
import time
import random
import os
from TestUnit.minibox.interface import Interface
from testframe.interface.interface_base import InterfaceBase

"""
测试条件：
* 至少接入一个mini box
* 至少存在一个event
"""
url = os.environ.get('AUTO_MINIBOX_URL', 'http://minibox_local_ui.turingvideo.cn:8081')


class MiniBoxConfig(unittest.TestCase, Interface):

    def setUp(self):
        param = {"username": "admin", "password": "admin123"}
        res = self.UserLogin(url, param)
        self.assertEqual(res['code'], 200, 'Login failed!')
        token = res['text']['data']['token']
        header = {'Authorization': 'Bearer ' + token}
        InterfaceBase(headers=header)
    # def tearDown(self):

    def test01TemperatureUnit(self):
        # Get Temperature unit
        res = self.GetTemperatureUnit(url)
        self.assertEqual(res['text']['code'], 0, 'Get temperature unit failed!')

        # Set Temperature unit
        u = res['text']['data']['temperature_unit']
        if u == 'f':
            unit = {"temperature_unit": "c"}
            unit1 = {"temperature_unit": "f"}
        else:
            unit = {"temperature_unit": "f"}
            unit1 = {"temperature_unit": "c"}

        sets = self.SetTemperatureUnit(url, unit)
        self.assertEqual(sets['text']['code'], 0, 'Temperature unit changed failed!')

        # restore
        self.SetTemperatureUnit(url, unit1)

    def test02CurrentTimezone(self):
        res = self.GetCurrentTimezone(url)
        self.assertEqual(res['text']['code'], 0, 'Get current timezone failed!')

        # Set current timezone
        u = res['text']['data']['timezone']
        if u == 'Asia/Shanghai':
            timezone = {"timezone": "America/Los_Angeles"}
        else:
            timezone = {"timezone": "Asia/Shanghai"}

        sets = self.SetCurrentTimezone(url, timezone)
        self.assertEqual(sets['text']['code'], 0, 'Current timezone changed failed!')

        # restore
        self.SetCurrentTimezone(url, res['text']['data'])

    def test03GetAllTimezones(self):
        # Get all timezones
        res = self.GetAllTimezones(url)

        self.assertEqual(res['text']['code'], 0, 'Get timezones failed!')

    def test04EventSavedTime(self):
        # Get event saved days
        res = self.GetEventSavedTime(url)
        self.assertEqual(res['text']['code'], 0, 'Get event saved hours failed!')

        # Set event saved days
        s = {"event_saved_hours": random.randint(0, 8760)}
        sets = self.SetEventSavedTime(url, s)
        self.assertEqual(sets['text']['code'], 0, 'Set event saved hours failed!')

        # restore
        self.SetEventSavedTime(url, res['text']['data'])

    def test05UploadConfig(self):
        # Get upload config
        res = self.GetUploadConfig(url)
        self.assertEqual(res['text']['code'], 0, 'Get upload config failed!')

        # Set upload config
        data = {"disable_cloud": True, "disable_upload_temperature": False, "disable_upload_picture": False}
        sets = self.SetUploadConfig(url, data)
        self.assertEqual(sets['text']['code'], 0, 'Update upload config failed!')

        # restore
        self.SetUploadConfig(url, res['text']['data'])


class MiniBoxCameras(unittest.TestCase, Interface):
    @classmethod
    def setUpClass(self):
        MiniBoxCameras.sn = None

    def test01GetCameras(self):
        #  Get all the camera information
        res = self.GetCameras(url)
        for i in res['text']['data']:
            if i['device_sn']:
                MiniBoxCameras.sn = i['device_sn']
                break
        self.assertEqual(res['text']['code'], 0, 'Get cameras information failed!')

    def test02RetrieveCameras(self):
        self.assertNotEqual(MiniBoxCameras.sn, None, 'Please add camera sn!')
        #  Get all the camera information
        res = self.RetrieveCameras(url, MiniBoxCameras.sn)

        self.assertEqual(res['text']['code'], 0, 'Retrieve camera information failed!')

    def test03SettingForCamera(self):
        self.assertNotEqual(MiniBoxCameras.sn, None, 'Please add camera sn!')
        # Get settings for a camera
        res = self.GetSettingForCamera(url, MiniBoxCameras.sn)
        self.assertEqual(res['text']['code'], 0, 'Get settings failed!')

        # Modify settings for a camera. Must request as a whole
        data = {"limit": 38.25, "outdoor": False, "range_min": 35, "range_max": 43.5, "fahrenheit_unit": True}
        sets = self.SetSettingForCamera(url, MiniBoxCameras.sn, data)
        self.assertEqual(sets['text']['code'], 0, 'Set settings failed!')

        # restore
        self.SetSettingForCamera(url, MiniBoxCameras.sn, res['text']['data'])

    def test04VolumeForCamera(self):
        self.assertNotEqual(MiniBoxCameras.sn, None, 'Please add camera sn!')
        # Get volume for this camera
        res = self.GetVolumeForCamera(url, MiniBoxCameras.sn)
        self.assertEqual(res['text']['code'], 0, 'Get volume failed!')

        # Set volume for this camera
        s = {"volume": random.randint(50, 80)}
        sets = self.SetVolumeForCamera(url, MiniBoxCameras.sn, s)
        self.assertEqual(sets['text']['code'], 0, 'Set volume failed!')

        # restore
        self.SetVolumeForCamera(url, MiniBoxCameras.sn, res['text']['data'])


class MiniBoxEvent(unittest.TestCase, Interface):
    @classmethod
    def setUpClass(self):
        MiniBoxEvent.eventId = None

    def test01GetEvents(self):
        # View all alarm events
        res = self.GetEvents(url)
        self.assertEqual(res['text']['code'], 0, 'View events failed!')

        for i in res['text']['data']:
            if i['id']:
                MiniBoxEvent.eventId = i['id']
                break

    def test02GetEvent(self):
        self.assertNotEqual(MiniBoxEvent.eventId, None, 'Please generate events!')
        res = self.GetEvent(url, MiniBoxEvent.eventId)
        self.assertEqual(res['text']['code'], 0, 'View an event failed!')

    def test03RetrieveEvent(self):
        self.assertNotEqual(MiniBoxEvent.eventId, None, 'Please generate events!')
        # View an event information
        res = self.RetrieveEvent(url, MiniBoxEvent.eventId)
        if self.check_json(res.text):
            import json
            p = {
                "code": res.status_code,
                "ec": 1,
                "text": json.loads(res.text)
            }
            self.loggers.error("Request Failed, return parameters:" + str(res.text))
        else:
            self.loggers.debug("Request successful.")
            p = {
                "code": res.status_code,
                "ec": 0
            }
        self.assertEqual(p['ec'], 0, 'View an event failed!')

    def test04DelEvent(self):
        self.assertNotEqual(MiniBoxEvent.eventId, None, 'Please generate events!')
        # View all alarm events
        res = self.DelEvent(url, MiniBoxEvent.eventId)
        self.assertEqual(res['text']['code'], 0, 'Delete an event failed!')

    def test05DelEvents(self):
        # Delete event by parameters
        st = (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        params = ["st=" + st, "et=" + "2020-01-01 16:34:06", "sn=test_sn"]
        param = random.choice(params)

        res = self.DelEvents(url, param)
        self.assertEqual(res['text']['code'], 0, 'Delete events failed!')


if __name__ == '__main__':
    unittest.main()

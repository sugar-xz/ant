import os
import copy
import random
from TestUnit.superbox.interfaces import Interfaces
from TestUnit.superbox.params import *


class Unit(object):
    base_path = os.path.dirname(__file__)
    url = os.environ.get('AUTO_SUPERBOX_URL', 'http://127.0.0.1:8000')
    apis = Interfaces(url)

    @classmethod
    def algorithmsImport(cls):
        file_path = cls.base_path + '/fixtures/algo.json'
        res = cls.apis.algorithmsImport('algo.json', file_path)
        exist, value = cls.apis.verify_result(res, 'dm')

        assert exist and value == 'ok', 'Import failed !!'

    @classmethod
    def camerasList(cls):
        mode = ['on', 'off', 'schedule']
        status = ['online', 'offline']
        choice = {'name': 'test', 'mode': random.choice(mode), 'status': random.choice(status)}
        param = cls.apis.random_params(choice)
        res = cls.apis.camerasList(param=param)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def cameraCreate(cls, camera_name=None):
        body = CREATE_CAMERA
        if camera_name is not None:
            body['name'] = camera_name
        res = cls.apis.cameraCreate(body)
        assert res['code'] == 201, 'Failed!'
        camera_id = res['text']['ret']['id']
        return camera_id

    @classmethod
    def cameraUpdate(cls, camera_id):
        body = copy.deepcopy(CREATE_CAMERA)
        body["mode"] = 'on'
        res = cls.apis.cameraUpdate(camera_id, body)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def cameraUpdatePart(cls, camera_id):
        body = cls.apis.random_params(CREATE_CAMERA)
        res = cls.apis.cameraUpdatePart(camera_id, body)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def camerasMode(cls, camera_id, params=None):
        if params is None:
            params = {}
            modes = ['on', 'off', 'schedule']
            params['mode'] = random.choice(modes)
        ids = [camera_id, 33]
        res = cls.apis.camerasMode(ids, params)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def eventsList(cls):
        pa = {'types': 'person'}
        pa = cls.apis.random_params(pa)
        res = cls.apis.eventsList(param=pa)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def eventCreate(cls, camera_id=None):
        body = CREATE_EVENT
        if camera_id is not None:
            body['camera_id'] = camera_id
        res = cls.apis.eventCreate(body)
        assert res['code'] == 201, 'Failed!'
        event_id = res['text']['ret']['id']
        return event_id

    @classmethod
    def eventUpdate(cls, event_id):
        body = cls.apis.random_params(PATCH_EVENT)
        res = cls.apis.eventUpdatePart(event_id, body)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def eventRetrieves(cls):
        num = random.randint(1, 8)
        choice = {'start_id': num, 'limit': num}
        param = cls.apis.random_params(choice)
        res = cls.apis.eventsRetrieves(param)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def eventRetrieve_ids(cls):
        choice = {'start_id': 1}
        res = cls.apis.eventsRetrieves(choice)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def mediumCreate(cls, event_id, mediums_name='snapshot'):
        """
        :param event_id:
        :param mediums_name: snapshot/video/bbox
        :return:
        """
        body, file_name, file_path = cls._medium_choice(event_id, mediums_name)
        res = cls.apis.mediumCreate(body, file_name, file_path)

        exist, medium_id = cls.apis.verify_result(res, 'id')
        assert exist, 'Failed !!'
        return medium_id

    @classmethod
    def mediumUpdate(cls, medium_id, mediums_name='snapshot', event_id=None):
        body, file_name, file_path = cls._medium_choice(event_id, mediums_name)
        res = cls.apis.mediumUpdate(medium_id, body, file_name, file_path)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def mediumUpdatePart(cls, medium_id, mediums_name='snapshot', event_id=None):
        body, file_name, file_path = cls._medium_choice(event_id, mediums_name)
        patch_body = cls.apis.random_params(body)
        res = cls.apis.mediumUpdatePart(medium_id, patch_body, file_name, file_path)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def _medium_choice(cls, event_id, mediums_name):
        names = {'snapshot': 'demo.jpeg', 'video': 'demo.mp4', 'bbox': 'demo.jpeg'}
        file_name = names[mediums_name]
        body = {'name': mediums_name, 'event_id': event_id}
        if event_id is None:
            del body['event_id']
        file_path = cls.base_path + '/fixtures/' + file_name
        return body, file_name, file_path

    @classmethod
    def ruleCreate(cls, camera_id=None):
        body = CREATE_RULE
        if camera_id is not None:
            body['camera'] = camera_id
        res = cls.apis.ruleCreate(body)
        exist, rule_id = cls.apis.verify_result(res, 'id')
        assert exist, 'Failed !!'
        return rule_id

    @classmethod
    def ruleUpdatePart(cls, rule_id, camera_id=None):
        body = CREATE_RULE
        if camera_id is not None:
            body['camera'] = camera_id
        patch_body = cls.apis.random_params(body)
        res = cls.apis.ruleUpdatePart(rule_id, patch_body)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def sampleCreate(cls, sample_id=None, camera_id=None):
        body = CREATE_SAMPLE
        if sample_id is not None:
            body['id'] = sample_id
        if camera_id is not None:
            body['camera_id'] = camera_id
        res = cls.apis.sampleCreate(body)
        exist, sample_id = cls.apis.verify_result(res, 'id')
        assert exist, 'Failed !!'
        return sample_id

    @classmethod
    def sampleUpdate(cls, sample_id=None):
        body = copy.deepcopy(CREATE_SAMPLE)
        if sample_id is not None:
            body['id'] = sample_id
        body['types'] = 'person:513'
        res = cls.apis.sampleUpdate(CREATE_SAMPLE['id'], body)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def sampleUpdatePart(cls, sample_id=None):
        if sample_id is not None:
            CREATE_SAMPLE['id'] = sample_id
        res = cls.apis.sampleUpdatePart(CREATE_SAMPLE['id'], CREATE_SAMPLE)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def sampleUpload_file(cls, sample_id=None):
        names = ['demo.jpeg', 'demo.mp4']
        name_key = names[random.randint(0, 1)]
        body = SAMPLE_UPLOAD_FILE
        if sample_id is not None:
            body['id'] = sample_id
        file_path = cls.base_path + '/fixtures/' + name_key
        res = cls.apis.sampleUpload_file(body['id'], name_key, file_path)
        assert res['code'] == 201, 'Failed!'

    @classmethod
    def settingCreate(cls, value=None, name=None):
        body = CREATE_SETTING
        if value is not None:
            body['value'] = value
        if name is not None:
            body['name'] = name
        res = cls.apis.settingCreate(body)
        exist, setting_id = cls.apis.verify_result(res, 'id')
        assert exist and res['text']['ret']['name'] == body['name'], 'Failed !!'
        return setting_id

    @classmethod
    def settingUpdatePart(cls, setting_id, value=None, name=None):
        body = CREATE_SETTING
        if value is not None:
            body['value'] = value
        if name is not None:
            body['name'] = name
        res = cls.apis.settingUpdatePart(setting_id, body)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def settingItemList(cls, name=None):
        param = {'name': name}
        res = cls.apis.settingItemList(param)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def settingItem(cls, value=None, name=None):
        body = CREATE_SETTING
        if value is not None:
            body['value'] = value
        if name is not None:
            body['name'] = name
        res = cls.apis.settingItem(body)
        assert res['code'] == 200, 'Failed!'

    @classmethod
    def webhookCreate(cls):
        res = cls.apis.settingItem(CREATE_WEBHOOK)
        exist, setting_id = cls.apis.verify_result(res, 'id')
        assert exist, 'Failed !!'
        return setting_id

    @classmethod
    def webhookUpdatePart(cls):
        body = cls.apis.random_params(CREATE_WEBHOOK)
        res = cls.apis.webhookUpdatePart(body)
        assert res['code'] == 200, 'Failed!'

Unit.algorithmsImport()
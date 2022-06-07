from testframe.interface.interface_base import InterfaceBase
from config.setting import API_VERSION


class Interfaces(InterfaceBase):

    def __init__(self, host):
        self.algorithms = host + "/api/" + API_VERSION + "/algorithms"
        self.cameras = host + "/api/" + API_VERSION + "/cameras"
        self.events = host + "/api/" + API_VERSION + "/events"
        self.mediums = host + "/api/" + API_VERSION + "/mediums"
        self.rules = host + "/api/" + API_VERSION + "/rules"
        self.samples = host + "/api/" + API_VERSION + "/samples"
        self.settings = host + "/api/" + API_VERSION + "/settings"
        self.webhooks = host + "/api/" + API_VERSION + "/webhooks"

    def algorithmsList(self):
        return self.Get(self.algorithms)

    def algorithmsImport(self, filename, file_path):
        url = self.algorithms + "/upload"
        return self.UpdateFiles(url, {}, filename, file_path, file_param_name="algo_file")

    def camerasList(self, param=None):
        """
        :param param: name/mode/status
        :return:
        """
        return self.Get(self.cameras, params=param)

    def cameraCreate(self, body):
        return self.Post(self.cameras, body)

    def cameraRetrieve(self, camera_id):
        url = self.cameras + '/' + str(camera_id)
        return self.Get(url)

    def cameraUpdate(self, camera_id, body):
        url = self.cameras + '/' + str(camera_id)
        return self.Put(url, body)

    def cameraUpdatePart(self, camera_id, body):
        url = self.cameras + '/' + str(camera_id)
        return self.Patch(url, body)

    def cameraDelete(self, camera_id):
        url = self.cameras + '/' + str(camera_id)
        return self.Delete(url)

    def camerasGet_all(self):
        url = self.cameras + "/get_all"
        return self.Get(url)

    def camerasMode(self, body, param):
        """
        :param body: cameras ids, example: [1,2]
        :param param: {"mode": "on/off"}
        :return:
        """
        url = self.cameras + "/mode"
        return self.Post(url, body, params=param)

    def camerasEnableSampling(self, body=None):
        if body is None:
            body = {}
        url = self.cameras + "/all_enable_sampling"
        return self.Post(url, body)

    def camerasDisableSampling(self, body=None):
        if body is None:
            body = {}
        url = self.cameras + "/all_disable_sampling"
        return self.Post(url, body)

    def camerasRestart_all(self, body=None):
        if body is None:
            body = {}
        url = self.cameras + "/restart_all"
        return self.Post(url, body)

    def camerasAlgorithmsList(self):
        url = self.cameras + "/algorithms"
        return self.Get(url)

    def eventsList(self, param=None):
        """
        :param param: types/camera_id
        :return:
        """
        return self.Get(self.events, params=param)

    def eventCreate(self, body):
        return self.Post(self.events, body)

    def eventsDelete(self, body=None):
        if body is None:
            body = {}
        url = self.events + "/delete_all"
        return self.Post(url, body)

    def eventRetrieve(self, event_id):
        url = self.events + '/' + str(event_id)
        return self.Get(url)

    def eventUpdatePart(self, event_id, body):
        url = self.events + '/' + str(event_id)
        return self.Patch(url, body)

    def eventDelete(self, event_id):
        url = self.events + '/' + str(event_id)
        return self.Delete(url)

    def eventsRetrieves(self, param=None):
        """
        :param param: Id at the beginning of the query {"start_id":1}
        :return:
        """
        url = self.events + "/retrieves"
        return self.Get(url, params=param)

    def eventsRetrieve_ids(self, param):
        """
        :param param: Event id less than {"start_id":1}
        :return:
        """
        url = self.events + "/retrieve_ids"
        return self.Get(url, params=param)

    def eventsUnmarked(self):
        url = self.events + "/unmarked"
        return self.Get(url)

    def mediumsList(self, param=None):
        return self.Get(self.mediums, params=param)

    def mediumCreate(self, body, filename, file_path):
        return self.UpdateFiles(self.mediums, body, filename, file_path)

    def mediumRetrieve(self, medium_id):
        url = self.mediums + '/' + str(medium_id)
        return self.Get(url)

    def mediumUpdate(self, medium_id, body, filename, file_path):
        url = self.mediums + '/' + str(medium_id)
        return self.UpdateFiles(url, body, filename, file_path, method='put')

    def mediumUpdatePart(self, medium_id, body, filename, file_path):
        url = self.mediums + '/' + str(medium_id)
        return self.UpdateFiles(url, body, filename, file_path, method='patch')

    def mediumDelete(self, medium_id):
        url = self.mediums + '/' + str(medium_id)
        return self.Delete(url)

    def rulesList(self, param=None):
        return self.Get(self.rules, params=param)

    def ruleCreate(self, body):
        return self.Post(self.rules, body)

    def ruleRetrieve(self, rule_id):
        url = self.rules + '/' + str(rule_id)
        return self.Get(url)

    def ruleUpdate(self, rule_id, body):
        url = self.rules + '/' + str(rule_id)
        return self.Put(url, body)

    def ruleUpdatePart(self, rule_id, body):
        url = self.rules + '/' + str(rule_id)
        return self.Patch(url, body)

    def ruleDelete(self, rule_id):
        url = self.rules + '/' + str(rule_id)
        return self.Delete(url)

    def samplesList(self, param=None):
        return self.Get(self.samples, params=param)

    def sampleCreate(self, body):
        return self.Post(self.samples, body)

    def sampleRetrieve(self, sample_id):
        url = self.samples + '/' + str(sample_id)
        return self.Get(url)

    def sampleUpdate(self, sample_id, body):
        url = self.samples + '/' + str(sample_id)
        return self.Put(url, body)

    def sampleUpdatePart(self, sample_id, body):
        url = self.samples + '/' + str(sample_id)
        return self.Patch(url, body)

    def sampleDelete(self, sample_id):
        url = self.samples + '/' + str(sample_id)
        return self.Delete(url)

    def sampleUpload_file(self, sample_id, body, filename, file_path):
        url = self.samples + '/' + str(sample_id) + "/upload_file"
        return self.UpdateFiles(url, body, filename, file_path, file_param_name='path')

    def settingsList(self, param=None):
        return self.Get(self.settings, params=param)

    def settingCreate(self, body):
        return self.Post(self.settings, body)

    def settingRetrieve(self, setting_id):
        url = self.settings + '/' + str(setting_id)
        return self.Get(url)

    def settingUpdate(self, setting_id, body):
        url = self.settings + '/' + str(setting_id)
        return self.Put(url, body)

    def settingUpdatePart(self, setting_id, body):
        url = self.settings + '/' + str(setting_id)
        return self.Patch(url, body)

    def settingDelete(self, setting_id):
        url = self.settings + '/' + str(setting_id)
        return self.Delete(url)

    def settingItemList(self, param):
        """
        :param param: {'name': 'setting_name'}
        :return:
        """
        url = self.settings + "/item"
        return self.Get(url, params=param)

    def settingItem(self, body):
        url = self.settings + "/item"
        return self.Post(url, body)

    def settingSet(self, body, param):
        url = self.settings + "/set"
        return self.Post(url, body, params=param)

    def webhooksList(self, param=None):
        return self.Get(self.webhooks, params=param)

    def webhookCreate(self, body):
        return self.Post(self.webhooks, body)

    def webhookRetrieve(self, hook_id):
        url = self.webhooks + '/' + str(hook_id)
        return self.Get(url)

    def webhookUpdate(self, hook_id, body):
        url = self.webhooks + '/' + str(hook_id)
        return self.Put(url, body)

    def webhookUpdatePart(self, hook_id, body):
        url = self.webhooks + '/' + str(hook_id)
        return self.Patch(url, body)

    def webhookDelete(self, hook_id):
        url = self.webhooks + '/' + str(hook_id)
        return self.Delete(url)

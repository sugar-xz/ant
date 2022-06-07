from testframe.interface.interface_base import InterfaceBase


class Interface(InterfaceBase):

    def UserLogin(self, host, param):
        url = host + "/api/login"
        result = self.Post(url, param)
        return result

    def GetTemperatureUnit(self, host):
        url = host + "/api/config/t"
        result = self.Get(url)
        return result

    def SetTemperatureUnit(self, host, param):
        url = host + "/api/config/t"
        result = self.Post(url, param)
        return result

    def GetCurrentTimezone(self, host):
        url = host + "/api/config/timezone"
        result = self.Get(url)
        return result

    def SetCurrentTimezone(self, host, param):
        url = host + "/api/config/timezone"
        result = self.Post(url, param)
        return result

    def GetAllTimezones(self, host):
        url = host + "/api/config/timezones"
        result = self.Get(url)
        return result

    def GetEventSavedTime(self, host):
        # Get event saved hours
        url = host + "/api/config/event_saved_time"
        result = self.Get(url)
        return result

    def SetEventSavedTime(self, host, param):
        # Set event saved hours
        url = host + "/api/config/event_saved_time"
        result = self.Post(url, param)
        return result

    def GetUploadConfig(self, host):
        url = host + "/api/config/upload"
        result = self.Get(url)
        return result

    def SetUploadConfig(self, host, param):
        url = host + "/api/config/upload"
        result = self.Post(url, param)
        return result

    def GetCameras(self, host):
        #  Get all the camera information
        url = host + "/api/cameras"
        result = self.Get(url)
        return result

    def RetrieveCameras(self, host, sn):
        url = host + "/api/cameras/" + str(sn)
        result = self.Get(url)
        return result

    def GetSettingForCamera(self, host, sn):
        url = host + "/api/cameras/" + str(sn) + "/settings"
        result = self.Get(url)
        return result

    def SetSettingForCamera(self, host, sn, param):
        # Modify settings for a camera. Must request as a whole
        url = host + "/api/cameras/" + str(sn) + "/settings"
        result = self.Post(url, param)
        return result

    def GetVolumeForCamera(self, host, sn):
        url = host + "/api/cameras/" + str(sn) + "/volume"
        result = self.Get(url)
        return result

    def SetVolumeForCamera(self, host, sn, param):
        # Modify settings for a camera. Must request as a whole
        url = host + "/api/cameras/" + str(sn) + "/volume"
        result = self.Post(url, param)
        return result

    def GetEvents(self, host):
        url = host + "/api/events"
        result = self.Get(url)
        return result

    def DelEvents(self, host, param):
        # Delete event by parameters
        """
        :param host:
        :param param: st;et;sn
        :return:
        """
        url = host + "/api/events"
        result = self.Delete(url, param)
        return result

    def GetEvent(self, host, eventId):
        url = host + "/api/events/" + str(eventId)
        result = self.Get(url)
        return result

    def DelEvent(self, host, eventId):
        url = host + "/api/events/" + str(eventId)
        result = self.Delete(url)
        return result

    def RetrieveEvent(self, host, eventId):
        url = host + "/api/events/" + str(eventId) + "/pic"
        data = {
            "method": "get",
            "url": url
        }
        result = self.request(data)
        return result

import json
import asyncio
import websockets
from testframe.common.base_common import BaseCommon


class WS(BaseCommon):
    def __init__(self, url, messages, headers=None):
        self.url = url
        self.messages = messages
        self.headers = headers

    def ws_connect(self):
        try:
            asyncio.get_event_loop().run_until_complete(self._app_connect(self.messages, self.headers))
        except Exception as e:
            self.loggers.error("Error: %s" % e)

    async def _app_connect(self, message, cookie):
        async with websockets.connect(self.url, extra_headers=cookie) as websocket:
            for item in message:
                # This works fine - sends a message
                self.loggers.debug("sending...")
                await websocket.send(json.dumps(item))
                self.loggers.debug("> {}".format(item))

                # This stops at the await and never receives
                try:
                    self.loggers.debug("receiving...")
                    # This is the line that causes sadness
                    data = await websocket.recv()
                    self.loggers.debug("< {}".format(data))
                except:
                    # This doesn't happen either
                    self.loggers.error("Listener is dead")


if __name__ == '__main__':
    req = [{
        "id": "abc",
        "act": "box.debug_echo",
        "arg": {"box_id": "box_dog_sr_50006"}
    }]
    url = 'http://192.168.2.138:8000/api/v1/user/auth/login'
    jsons = {"username": "customer@turingvideo.net", "password": "1234qwer"}
    import requests
    from testframe.interface.interface_test import InterfaceTest
    res = InterfaceTest().run('post', url, body=jsons)
    res_cookies = requests.utils.dict_from_cookiejar(res['response'].cookies)
    cookies = BaseCommon.cookies_to_string(res_cookies)
    cookie = {'Cookie': cookies}
    WS('ws://192.168.2.138:8000', req, headers=cookie).ws_connect()

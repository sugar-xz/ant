#!/usr/bin/python
import requests
import base64
import json
import random
from urllib3 import encode_multipart_formdata

from config.setting import AUTO_CSRFTOKEN
from testframe.common.base_common import BaseCommon


class InterfaceBase(BaseCommon):
    default_session = requests.session()
    exist = False
    v = None

    def __init__(self, headers=None):
        if headers is not None:
            self.default_session.headers.update(headers)

    def Get(self, url, params=None, headers=None, coding=False):
        if coding:
            params = self.base64Encode(json.dumps(params))
        data = {
            "method": "get",
            "url": url,
            "headers": headers,
            "params": params
        }
        r = self.request(data)

        return self.result(r, base64_code=coding)

    def Post(self, url, body, params=None, headers=None, coding=False):
        if coding:
            params = self.base64Encode(json.dumps(body))
        data = {
            "method": "post",
            "url": url,
            "headers": headers,
            "params": params,
            "body": body
        }
        r = self.request(data)

        return self.result(r, base64_code=coding)

    def UpdateFiles(self, url, body, filename, file_path, file_param_name="file", method='post'):
        """
        :param body: All parameters except `file` in the request
        :param filename: File name
        :param file_path: The absolute path of the file
        :return:
        """
        with open(file_path, mode="rb")as f:
            body[file_param_name] = (filename, f.read())
            encode_data = encode_multipart_formdata(body)
            file_data = encode_data[0]
            headers_from_data = {
                "Content-Type": encode_data[1],
            }
            data = {
                "method": method,
                "url": url,
                "headers": headers_from_data,
                "body": file_data,
            }
            r = self.request(data)

        return self.result(r)

    def Put(self, url, body, headers=None):
        data = {
            "method": "put",
            "url": url,
            "headers": headers,
            "body": body
        }
        r = self.request(data)

        return self.result(r)

    def Patch(self, url, body, headers=None):
        data = {
            "method": "patch",
            "url": url,
            "headers": headers,
            "body": body
        }
        r = self.request(data)

        return self.result(r)

    def Delete(self, url, params=None, headers=None):
        data = {
            "method": "delete",
            "url": url,
            "headers": headers,
            "params": params
        }
        r = self.request(data)

        return self.result(r)

    def request(self, apiData, session=default_session):
        """
        :param session:
        :param apiData:
            {
                "method": "",
                "url": "",
                "headers": {},
                "params": {},
                "body": {}
            }
        :param method: get options head post put patch delete
        :return:
        """
        try:
            method = apiData["method"]

            url = apiData["url"]

            h = apiData.get("headers", None)
            if h is None:
                h = {"Content-Type": "application/json"}
            if "Content-Type" not in h.keys():
                h["Content-Type"] = "application/json"

            #   website sessionID for login
            if AUTO_CSRFTOKEN:
                res_cookies = requests.utils.dict_from_cookiejar(session.cookies)
                if len(res_cookies) != 0:
                    if "csrftoken" in res_cookies.keys():
                        h["X-CSRFTOKEN"] = res_cookies["csrftoken"]

            p = apiData.get("params", None)

            body = apiData.get("body", None)
            if body is not None and not isinstance(body, bytes):
                if not self.check_json(body):
                    body = json.dumps(apiData["body"])

            self.loggers.debug("Request parameter:" + str(apiData))

            re = session.request(method=method, url=url, headers=h, params=p, data=body, verify=False)
            # verify=false 取消警告
            return re
        except requests.exceptions.RequestException as e:
            self.loggers.error("request:" + str(e))
        except json.decoder.JSONDecodeError as e:
            self.loggers.error("json:" + str(e))
        except IOError as e:
            self.loggers.error("io:" + str(e))
        except (Exception, TypeError) as e:
            self.loggers.error(e)

    def result(self, result, base64_code=False):
        if result is not None:
            if base64_code:
                p = {
                    "code": result.status_code,
                    "text": self.base64Decode(result.text)
                }
            elif self.check_json(result.text):
                p = {
                    "code": result.status_code,
                    "text": json.loads(result.text)
                }

            else:
                p = {
                    "code": result.status_code,
                    "text": str(result.text)
                }
        else:
            p = {
                "code": str(result.status_code),
                "text": str(result)
            }
        if result.status_code in [200, 201, 203, 204, 205]:
            if base64_code:
                self.loggers.debug("Request successful, return parameters:" + self.base64Decode(result.text))
            else:
                self.loggers.debug("Request successful, return parameters:" + str(result.text))
        else:
            self.loggers.error("Request failed，" + str(p))
        return p

    def check_json(self, input_str):
        try:
            json_object = json.loads(input_str)
            return True
        except:
            return False

    # 功能:解密/加密
    # 作者:sugar
    # 时间:2018.02.13
    def base64Decode(self, s):
        try:
            return base64.b64decode(s)
        except BaseException as e:
            self.loggers.error(e)

    def base64Encode(self, s):
        try:
            return base64.b64encode(s)
        except BaseException as e:
            self.loggers.error(e)

    def config(self, path):
        File = self.readFile(path).split("\n")
        json = {}
        for config in File:
            if (config != ""):
                t = config.split("=")
                json[t[0]] = t[1]
        return json

    def readFile(self, path):
        try:
            f = open(path, 'r')
            return f.read()
        finally:
            if f:
                f.close()

    def verify_result(self, res, key):
        """
        :param res: dict
        :param key: The key to find
        :return:
        """
        is_exist, value = False, None
        code = res["code"]
        if 200 <= code < 300:
            is_exist, value = self._verify_result(res, key)
        return is_exist, value

    def _verify_result(self, data, key):
        for i in data:
            if i == key:
                self.exist = True
                self.v = data[i]
            if isinstance(data[i], dict):
                self._verify_result(data[i], key)
        return self.exist, self.v

    def random_params(self, data):
        try:
            # dict 随机取N个值
            ran_key = random.sample(data.keys(), random.randint(0, len(data)))
            re = dict()
            for key in ran_key:
                re[key] = data[key]
            return re
        except Exception:
            # list 随机取值
            if isinstance(data, list):
                res = random.choice(data)
                return res




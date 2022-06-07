#!/usr/bin/python
import time
import datetime
import requests
import base64
import json
from urllib3 import encode_multipart_formdata
from testframe.common.base_common import BaseCommon


class InterfaceTest(BaseCommon):

    def __init__(self):
        self.session = requests.session()

    def run(self, method, url, body=None, params=None, headers=None, cookies=None, file_body=None):
        """
        :param method: 'get','post','patch','put','delete'
        :param url: '(http/https)://route:port'
        :param params: {}
        :param body: {}
        :param headers: {}
        :param cookies: {'isClearCookie':False,'isSetCookie':{'csrftoken':'X-CSRFTOKEN','**':''***}}
        :param file_body: {'name':'','path':'','key':''}
        :return: {'testBaseInfo':'','testStartTime':'','response':'','spendingTimeInSec':'',
                    'responseHttpStatusCode':'','responseData':''}
        """
        test_case = dict()
        test_result = dict()

        test_case['method'] = method
        test_case['url'] = url
        test_case['params'] = params if params else None
        test_case['headers'] = headers if headers else None
        test_case['isClearCookie'] = cookies['isClearCookie'] if cookies and ('isClearCookie' in cookies) else False
        test_case['isSetCookie'] = cookies['isSetCookie'] if cookies and ('isSetCookie' in cookies) else None
        test_case['body'] = body if body else None
        if file_body:
            req_body, file_header = self._file_request(body, file_body)
            test_case['body'] = req_body
            test_case['headers'] = dict(test_case['headers'], **file_body) if headers else file_header
        if test_case['isSetCookie']:
            # Add sessionID for headers
            test_case['headers'] = self._set_cookies(test_case, test_case['headers'])
            test_case['headers'] = None if test_case['headers'] in ["", {}, {'': ''}] else test_case['headers']
        self.loggers.debug('Request parameters:  %s' % test_case)

        backup_test_start = time.time()
        test_start_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        obj_custom = self.execute_single_test(test_case)
        backup_test_end = time.time()
        backup_test_spending_time = round(backup_test_end - backup_test_start, 3)

        test_result['testBaseInfo'] = test_case
        test_result['testStartTime'] = test_start_datetime
        test_result['response'] = obj_custom['response']
        test_result['spendingTimeInSec'] = obj_custom['spendingTimeInSec'] if 'spendingTimeInSec' in obj_custom.keys() \
            else backup_test_spending_time
        return test_result

    def execute_single_test(self, test_case):

        compulsory_key_list = ['method', 'url']
        if not self._validate_test_params(compulsory_key_list, test_case):
            raise Exception('Missing required parameters!(method、url)  ')

        if test_case.get('isClearCookie', False):
            self.session.cookies.clear()
        session = self.session

        try:
            url = test_case.get('url')
            method = test_case.get('method')
            headers = test_case.get('headers')
            request_params = test_case.get('params')
            json_data = test_case.get('body')
        except BaseException as e:
            raise BaseException('Problem with test case format!  :%s' % e)

        try:
            use_json_data = len(list(filter(lambda x: str(x).lower() == 'content-type' and 'json'
                                                      in headers[x], headers.keys() if headers else {}))) > 0

            test_start = time.time()
            if use_json_data:
                response = session.request(url=url, method=method, params=request_params, json=json_data,
                                           headers=headers, verify=False)
            else:
                response = session.request(url=url, method=method, params=request_params, data=json_data,
                                           headers=headers, verify=False)

            test_end = time.time()
            test_spending_time = round(test_end - test_start, 3)
        except BaseException as e:
            raise BaseException('Request failed, error message: <%s> ' % e)

        obj_custom = dict()
        obj_custom['response'] = response
        obj_custom['spendingTimeInSec'] = test_spending_time
        obj_custom['responseHttpStatusCode'] = response.status_code

        try:
            obj_custom["responseData"] = response.content.encode("utf-8").decode("unicode-escape")
        except BaseException:
            obj_custom["responseData"] = response.text
        self.loggers.debug('Request successful:  %s' % obj_custom["responseData"])

        return obj_custom

    def _file_request(self, body, file_body):
        body = body if isinstance(body, dict) else json.loads(body)
        file_body = file_body if isinstance(file_body, dict) else json.loads(file_body)

        key_list = ['name', 'path', 'key']
        if self._validate_test_params(key_list, file_body):
            name = file_body['name']
            path = file_body['path']
            file_key = file_body['key']

            with open(path, mode="rb")as f:
                body[file_key] = (name, f.read())
                encode_data = encode_multipart_formdata(body)
                file_data = encode_data[0]
                headers_from_data = {
                    "Content-Type": encode_data[1],
                }
            return file_data, headers_from_data
        else:
            raise TypeError('Please confirm the file name, path and file parameter name！  ')

    def _validate_test_params(self, compulsory_key_list, items):
        return all([compulsory_key in items.keys() for compulsory_key in compulsory_key_list])

    def _set_cookies(self, case, headers):
        header = {}
        _set_cookies = case.get('isSetCookie')
        if _set_cookies and isinstance(_set_cookies, dict):
            res_cookies = requests.utils.dict_from_cookiejar(self.session.cookies)
            for cookie_key in _set_cookies.keys():
                if len(res_cookies) != 0 and cookie_key in res_cookies.keys():
                    header[_set_cookies[cookie_key]] = res_cookies[cookie_key]
        return {**headers, **header} if headers else header if header else None

    def _auto_set_cookies(self, headers):
        for key, value in self.session.cookies.items():
            headers[key] = value
        return headers

    def check_json(self, input_str):
        try:
            json_object = json.loads(input_str)
            return True
        except:
            return False

    def base64Decode(self, s):
        try:
            return base64.b64decode(s)
        except BaseException as e:
            raise BaseException('Format failed!  %s' % e)

    def base64Encode(self, s):
        try:
            return base64.b64encode(s)
        except BaseException as e:
            raise BaseException('Format failed!  %s' % e)


if __name__ == '__main__':
    pass


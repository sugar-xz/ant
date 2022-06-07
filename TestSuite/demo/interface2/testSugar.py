import unittest
import paramunittest
from testframe.common.base_common import BaseCommon
from .businessCommon import login
from testframe.interface.interface_base import InterfaceBase
deleteAddress_xls = BaseCommon.get_xls(["TestSutie", "demo", "interface2", "userCase.xlsx"], "test")


@paramunittest.parametrized(*deleteAddress_xls)
class DeleteAddress(unittest.TestCase):
    def setParameters(self, case_name, url, method, token, params, data, result, code, msg):
        """
        set params
        :param case_name:
        :param method:
        :param address_id:
        :param code:
        :param result:
        :param msg:
        :return:
        """
        self.case_name = str(case_name)
        self.url = str(url)
        self.method = str(method)
        self.token = str(token)
        self.params = str(params)
        self.data = str(data)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.info = None

    def description(self):
        """

        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        self.loggers = BaseCommon.loggers

    def testGetAddressList(self):
        """
        test body
        :return:
        """
        # get token
        # if self.token == '0':
        #     token = self.login_token
        # elif self.token == '1':
        #     token = localReadConfig.get_headers("TOKEN_U")
        # else:
        #     token = self.token

        # set headers
        header = login()

        # test interface
        self.return_json = InterfaceBase().Get(self.url, self.params, header)
        # self.return_json = get(self.url, self.params, header)

        # check result
        # self.checkResult()

    def tearDown(self):
        """

        :return:
        """
        self.loggers.info(self.case_name+" - Code:"+self.code+" - msg:"+self.msg)

    def checkResult(self):
        """
        check test result
        :return:
        """
        import json
        self.info = self.return_json.json()
        url = self.info.url
        msg = self.info.text
        print("\n请求地址：" + url)
        # 可以显示中文
        print("\n请求返回值：" + '\n' + json.dumps(json.loads(msg), ensure_ascii=False, sort_keys=True, indent=4))

        # if self.result == '0':
        #     self.assertEqual(self.info['code'], self.code)
        #     self.assertEqual(self.info['msg'], self.msg)
        #
        # if self.result == '1':
        #     self.assertEqual(self.info['code'], self.code)
        #     self.assertEqual(self.info['msg'], self.msg)

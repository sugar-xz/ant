import os
import platform
from xlrd import open_workbook
from xml.etree import ElementTree as ElementTree

from config.setting import BASE_DIR
from testframe.common.config_util import ConfigUtil
from testframe.common.logger import Log
from testframe.common.send_mail import SendEmail


class BaseCommon:
    loggers = Log.get_log()
    logPath = Log.get_result_path()
    resultPath = Log.get_report_path()
    sendEmail = SendEmail.get_email()

    @classmethod
    def get_xls(cls, xls_name, sheet_name):
        """
        get interface data from xls file
        :return:
        """
        clss = []
        # get xls file's path
        xlsPath = cls.os_join_path(xls_name)
        # open xls file
        file = open_workbook(xlsPath)
        # get sheet by name
        sheet = file.sheet_by_name(sheet_name)
        # get one sheet's rows
        nrows = sheet.nrows
        for i in range(nrows):
            if sheet.row_values(i)[0] != u'case_name':
                clss.append(sheet.row_values(i))
        return clss

    @classmethod
    def get_url_from_xml(cls, name):
        """
        By name get url from interfaceURL.xml
        :param name: interface's url name
        :return: url
        """
        url_list = []
        url_path = cls.os_join_path(["TestSutie", "demo", "interface2", "config.ini"])
        tree = ElementTree.parse(url_path)
        for u in tree.findall('url'):
            url_name = u.get('name')
            if url_name == name:
                for c in u.getchildren():
                    url_list.append(c.text)
        u = ConfigUtil.get_ini("urls", "interface")
        url = u + '/'.join(url_list)
        return url

    @classmethod
    def os_join_path(cls, paths):
        file_path = BASE_DIR
        if isinstance(paths, list):
            for path in paths:
                file_path = os.path.join(file_path, path)
        else:
            file_path = os.path.join(BASE_DIR, paths)
        return file_path

    @classmethod
    def get_os_separator(cls):
        return '\\' if 'Windows' in platform.system() else '/'

    @classmethod
    def cookies_to_string(cls, cookies):
        return cls._cookies_to_string(cookies) if len(cookies) > 0 else None

    @classmethod
    def _cookies_to_string(cls, cookies):
        string = list()
        for k, v in cookies.items():
            string.append('%s=%s' % (k, v))
        return ';'.join(string)

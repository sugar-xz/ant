#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'Sugar'

import os
import sys
import logging
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)


# 配置文件
TEST_CONFIG = os.path.join(BASE_DIR, "config", "config.ini")

# Log configuration
AUTO_LOG_LEVEL = logging.DEBUG
AUTO_LOG_WRITE = os.environ.get("AUTO_LOG_WRITE", True)
# Whether to send mail
AUTO_REPORT_NAME = os.environ.get("AUTO_REPORT_NAME", "report")
REPORT_NAME = str(datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S_")) + AUTO_REPORT_NAME + '.html'
AUTO_SEND_EMAIL = os.environ.get("AUTO_SEND_EMAIL", False)

# TEST CASE
AUTO_CASE_FILE = os.environ.get("AUTO_CASE_FILE", "caselist.yml")
AUTO_CASE_PATH = os.environ.get("AUTO_CASE_PATH", "TestSuite")
AUTO_CASE_SUBSET = os.environ.get("AUTO_CASE_SUBSET", "basecase")
API_VERSION = os.environ.get("API_VERSION", "v1")

# Will be deprecated
# Website cookies
AUTO_CSRFTOKEN = os.environ.get("AUTO_CSRFTOKEN", False)
# 测试用例程序文件
TEST_CASE = os.path.join(BASE_DIR, "TestSuite", "demo", "unitest")
# 测试用例模板文件
SOURCE_FILE = os.path.join(BASE_DIR, "TestSuite", "demo", "interface1", "DemoAPITestCase.xlsx")
# excel测试用例结果文件
TARGET_FILE = os.path.join(BASE_DIR, "export", "excelReport", "DemoAPITestCase.xlsx")

# 驱动需自己手动下载对应版本，firefox下载放在安装目录
'''
火狐：https://github.com/mozilla/geckodriver/releases
谷歌：http://npm.taobao.org/mirrors/chromedriver/
'''
BROWSER_DRIVER = os.environ.get("BROWSER_DRIVER", None)


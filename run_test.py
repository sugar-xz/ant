import os
import re
import unittest
from config import setting
from testframe.common.base_common import BaseCommon
from testframe.extend import HTMLTestRunner
from testframe.common.config_util import ConfigUtil


class runTest(BaseCommon):
    def __init__(self):
        self.caseList = []
        self.caseListFile = BaseCommon.get_os_separator() + setting.AUTO_CASE_FILE
        self.caseDir = os.path.join(setting.BASE_DIR, setting.AUTO_CASE_PATH)
        # report
        self.title = ConfigUtil.get_ini("user", "SUBJECT")
        self.tester = ConfigUtil.get_ini("tester", "name")

    def set_case_list(self):
        """
        set case list
        :return:
        """
        cases = ConfigUtil.get_yml_all(self.caseListFile)
        subsets = setting.AUTO_CASE_SUBSET
        subset = re.split(',', subsets)
        for i in subset:
            self.caseList.extend(cases[i])

    def set_case_suite(self, case):
        """
        set case suite
        :return:
        """
        if case is None:
            self.set_case_list()
        else:
            self.caseList = case
        testunit = unittest.TestSuite()
        package_tests = []

        for case in self.caseList:
            case_name = case.split("/")[-1]
            self.loggers.debug("TestFile: " + case_name + ".py")
            discover = unittest.defaultTestLoader.discover(self.caseDir, pattern=case_name + '.py', top_level_dir=None)
            package_tests.append(discover)

        for test_suite in package_tests:
            for test_case in test_suite:
                testunit.addTests(test_case)
        return testunit

    def run(self, case=None, test_dir=None):
        """
        :param test_dir:
        :param case: ['TestSuite/demo/unitest/test_main','TestSuite/demo/unitest/main']
                    ['TestSuite/demo/unitest/test_*']
        :return: HTMLTestRunner.result
        """
        try:
            dir_list = test_dir.split('/') if test_dir else [setting.AUTO_CASE_PATH]
            caseDir = setting.BASE_DIR
            for i in dir_list:
                caseDir = os.path.join(caseDir, i)
            self.caseDir = caseDir

            suit = self.set_case_suite(case)
        except ImportError as e:
            self.loggers.error('Directory error: %s' % e)
            return {'err': 'The test directory does not exist!'}
        if suit._tests.__len__() == 0:
            self.loggers.error("Test file does not exist!")
            return

        self.loggers.info("********TEST START********")
        if setting.AUTO_LOG_WRITE:
            fp = open(self.resultPath, 'wb')
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=self.title,
                                                   description='Test case execution result', tester=self.tester)
        else:
            runner = HTMLTestRunner.HTMLTestRunner(title=self.title, description='Test case execution result',
                                                   tester=self.tester)
        result = runner.run(suit)
        self.loggers.info("*********TEST END*********")

        try:
            fp.close()
        except:
            pass
        # send test report by email
        if setting.AUTO_SEND_EMAIL:
            self.sendEmail.send_mail()
        else:
            self.loggers.debug("No send report email to developer.")
        return result


if __name__ == '__main__':
    obj = runTest()
    obj.run()

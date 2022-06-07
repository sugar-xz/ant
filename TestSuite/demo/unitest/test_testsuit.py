import unittest


# 执行测试的类
class UCTestCase(unittest.TestCase):
    def setUp(self):
        # 测试前需执行的操作
        pass

    def tearDown(self):
        # 测试用例执行完后所需执行的操作
        pass

        # 测试用例1

    def testCreateFolder(self):
        # 具体的测试脚本
        print(1111111111)

        # 测试用例2

    def testDeleteFolder(self):
        # 具体的测试脚本
        print(22222222222)


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(UCTestCase("testCreateFolder"))
    suite.addTest(UCTestCase("testDeleteFolder"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
import unittest


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
        print(11111111112)

    # 测试用例2
    def testDeleteFolder(self):
        # 具体的测试脚本
        print(222222222223)


if __name__ == "__main__":
    unittest.main()

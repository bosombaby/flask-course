import unittest
from hello import sayhello


class SayHelloTestCase(unittest.TestCase):  # 测试用例
    def setUp(self):  # 测试固件
        pass

    def tearDown(self):  # 测试固件
        pass

    def test_sayhello(self):  # 第 1 个测试
        rv = sayhello()
        self.assertEqual(rv, "Hello!")

    def test_sayhello_to_somebody(self):  # 第 2 个测试
        rv = sayhello(to="Grey")
        self.assertEqual(rv, "Hello, Grey!")


if __name__ == "__main__":
    unittest.main()

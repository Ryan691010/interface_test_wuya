import sys
sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\InterfaceTesting\env\Lib\site-packages")
import requests
import json
import unittest
import time as t
import os
import yaml
# from ddt import ddt,file_data
from api.page import user

# @ddt
class TestUserApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        t.sleep(1)

    @classmethod
    def tearDownClass(cls):
        pass
    def statusCode(self,r):
        '''对HTTP状态码和业务码进行校验'''
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.status_code, 200)
    def test_user_api_001(self):
        ''''登录系统'''
        r = requests.post(
            url=user.getUrl() + 'g/hsxone.omc/v/submitLogin',
            data=user.getDit()  # 将用户名密码用字典传入data而且不用加上headers
        )
        with open(r'C:\Users\zhongyc27701\PycharmProjects\interface_test_wuya\api\data\token', 'w') as f:
            f.write(r.json()["data"][0]["user_token"])
        # print(r.json())
        # print(r.json()["data"][0]["user_token"])
        self.assertEqual(r.status_code,200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
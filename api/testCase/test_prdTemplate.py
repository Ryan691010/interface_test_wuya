import json
import sys
sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\InterfaceTesting\env\Lib\site-packages")
import requests
import unittest
import time as t
from api.page import user
from api.page.getExcel import GetExcel
from api.page.getToken import getToken
from api.page.getNowtime import getNowtime
from api.page.forAddAssert import getAddnumber

class TestPrdApi(unittest.TestCase):
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

    def test_prdadd(self):
        '''新增产品模块'''
        # self.excelagur = GetExcel()
        # #获取要用到的url
        # act_url = self.excelagur.geturl(1)
        # print(GetExcel().geturl(1))
        # #获取要用到的headers
        # act_headers = self.excelagur.getheaders(1)
        # # print(act_headers)
        # #获取要用到的payloadData
        # act_payloaddata = self.excelagur.getpaylodData(1)
        # json_payloaddata = json.dumps(act_payloaddata)
        # print(json_payloaddata)
        r = requests.post(url = GetExcel().geturl(1),
                          data=json.dumps(GetExcel().getpaylodData(1)),
                          headers = GetExcel().getheaders(1)
                          )
        # print(json.dumps(r.json(),indent=True))
        # print(r.text)
        print(r.status_code)
        print(getAddnumber())
        self.statusCode(r)
        self.assertEqual(1,getAddnumber())




if __name__ == '__main__':
    unittest.main(verbosity=2)
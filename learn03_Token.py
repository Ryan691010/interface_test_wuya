import json
import sys

sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\InterfaceTesting\env\Lib\site-packages")
import requests
import unittest
# from api.page.getToken import getToken
from api.page.getNowtime import getNowtime


# def getHeaders():
#     headers = {
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'Connection': 'keep-alive',
#         'Content-Length': '42',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Cookie': 'token=3d318cb6-d401-4b63-ab80-5bd5c387dc3a2; lang=zh-CN',
#         'Host': '10.20.155.135:8088',
#         'Origin': 'http://10.20.155.135:8088',
#         'Referer': 'http://10.20.155.135:8088/bfam6/',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
#     }
#     return headers

def getUrl():
    return 'http://10.20.155.135:8088/'


# 登录的参数是form data格式，用一个字典封装
def loginData():
    dict1 = {
        'operator_code': 'zyc',
        'password': 'zyc111111=='
    }
    return dict1


# class Api(unittest.TestCase):
#     def statusCode(self,r):
#         self.assertEqual(r.json()['staus'],0)
#         self.assertEqual(r.status_code,200)
class Api(unittest.TestCase):
    # 断言
    # def statusCode(self,r):
    #     self.assertEqual(r.json()['code'],200)
    #     self.assertEqual(r.status_code,200)

    def test_api_001(self):
        '''登录系统'''
        r = requests.post(
            url=getUrl() + 'g/hsxone.omc/v/submitLogin',
            data=loginData()  # 将用户名密码用字典传入data而且不用加上headers
            # files = loginData()
            # headers = getHeaders()
        )
        print(getUrl() + 'g/hsxone.omc/v/submitLogin')
        print(json.dumps(r.json(), indent=True))
        print(r.status_code)
        # print(r.json()['code'])
        print(r.json()["data"][0]["user_token"])
        with open('token', 'w') as f:
            f.write(r.json()["data"][0]["user_token"])
        # self.assertEqual(r.json()['code'],20)
        self.assertEqual(r.status_code, 200)

    def getToken(self):
        '''读取token文件内容'''
        with open('token', 'r') as f:
            # print(f.read())
            return f.read()

    # 新增产品模块
    def getHeaders(self):
        headers = {'Accept': 'application/json, text/plain, */*',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9',
                   'Connection': 'keep-alive',
                   'Content-Length': '1279',
                   'Content-Type': 'application/json;charset=UTF-8',
                   'Cookie': 'token=' + self.getToken(),
                   'Host': '10.20.155.135:8088',
                   'Origin': 'http://10.20.155.135:8088',
                   'Referer': 'http://10.20.155.135:8088/bfam6/',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
        return headers

    payloadData = {"bankNo":"C1","interCustNo":"","prdSeries":"","prdCode":getNowtime(),"prdMinBala":"0.00","bfirsCode":"","spvCode":"","assetpoolCode":"","clientMinRate":"0.00000","prdName":"1307zyc模板","prdMaxBala":"0.00","clientMaxRate":"0.00000","redDays":"0","managerType":"","divDays":"0","clientAvgRate":"0.00000","trusteeDuties":"","clientTypeArr":[],"ipoStartDate":"","rhCreditOrgTypeArr":[],"saleChannelArr":[],"interestBrand":"","rhCreditTypeArr":[],"openMode":"","ipoEndDate":"","onBusinessTime":[],"estabDate":"","cooperation":"","openPeriod":"","allotShareRate":"0.00000000","modeType":"","redeemShareRate":"0.00000000","theoryEndDate":"","endDate":"","otheropenDay":"","jiancangPeriod":"0","capitalSafeFlag":"","openIrregular":"","pfirstAmt":"0.00","ofirstAmt":"0.00","payBasis":"","incomeBzflag":"","firstopenBdate":"","psubUnit":"0.00","guestRate":"0.00000","collectShare":"0.00000","fundAccCode":"","openHoliFlag":"","openNumbers":"0.00","osubUnit":"0.00","fundAccName":"","collectAmt":"0.00","reportFlag":"01","pminHold":"0.000","openBusiness":"","navDigit":"4","openBusinessDes":"","ominHold":"0.000","structFlag":"","navRule":"0","structType":"","incomeRightTransferFlag":"","zzsbMemo":"","modelFlag":"02","status":"","templateCode":"1307","dataStatus":"3","feeinfodata":[]}

    def test_prdadd(self):
        '''新增产品模块'''
        r = requests.post(url='http://10.20.155.135:8088/productmanage/prdadd',
                          # json = self.payloadData,
                          data=json.dumps(self.payloadData),  # 效果同上
                          headers=self.getHeaders()
                          )
        print('token是' + self.getToken())
        # print(json.dumps(r.json(),indent=True))
        p = self.payloadData
        h = self.getHeaders()
        print(type(json.dumps(self.payloadData)))
        print(json.dumps(self.payloadData))
        print(type(p))
        print(p)
        print(type(h))
        print(h)
        print(r.text)
        print(r.status_code)
        # self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)

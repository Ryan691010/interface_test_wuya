import sys
sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\InterfaceTesting\env\Lib\site-packages")
import requests
import json
import urllib3
urllib3.disable_warnings()

def getHeaders():
    headers = {'Accept':'application/json, text/plain, */*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language' : 'zh-CN,zh;q=0.9',
'Connection' : 'keep-alive',
'Content-Length':'1277',
'Content-Type':'application/json;charset=UTF-8',
'Cookie':'token=033cfce0-9279-4103-a933-de0f6ab575bc2',
'Host':'10.20.155.135:8088',
'Origin':'http://10.20.155.135:8088',
'Referer':'http://10.20.155.135:8088/bfam6/',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    return headers

payloadData = {"bankNo":"C1","interCustNo":"","prdSeries":"","prdCode":"zyc6707","prdMinBala":"0.00","bfirsCode":"","spvCode":"","assetpoolCode":"","clientMinRate":"0.00000","prdName":"zyc6702模板","prdMaxBala":"0.00","clientMaxRate":"0.00000","redDays":"0","managerType":"","divDays":"0","clientAvgRate":"0.00000","trusteeDuties":"","clientTypeArr":[],"ipoStartDate":"","rhCreditOrgTypeArr":[],"saleChannelArr":[],"interestBrand":"","rhCreditTypeArr":[],"openMode":"","ipoEndDate":"","onBusinessTime":[],"estabDate":"","cooperation":"","openPeriod":"","allotShareRate":"0.00000000","modeType":"","redeemShareRate":"0.00000000","theoryEndDate":"","endDate":"","otheropenDay":"","jiancangPeriod":"0","capitalSafeFlag":"","openIrregular":"","pfirstAmt":"0.00","ofirstAmt":"0.00","payBasis":"","incomeBzflag":"","firstopenBdate":"","psubUnit":"0.00","guestRate":"0.00000","collectShare":"0.00000","fundAccCode":"","openHoliFlag":"","openNumbers":"0.00","osubUnit":"0.00","fundAccName":"","collectAmt":"0.00","reportFlag":"01","pminHold":"0.000","openBusiness":"","navDigit":"4","openBusinessDes":"","ominHold":"0.000","structFlag":"","navRule":"0","structType":"","incomeRightTransferFlag":"","zzsbMemo":"","modelFlag":"02","status":"","templateCode":"1307","dataStatus":"3","feeinfodata":[]}

def prdadd():
    r = requests.post(url = 'http://10.20.155.135:8088/productmanage/prdadd',
                     json = payloadData,
                      # data = json.dumps(payloadData),#效果同上
                      headers = getHeaders()
                     )
    print(json.dumps(r.json(),indent=True))
    print(r.status_code)
    print(r.text)

if __name__ == '__main__':
    prdadd()
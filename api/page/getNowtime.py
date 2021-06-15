import time
'''获取当前时间'''
def getNowtime():

    payloadData = {"bankNo":"C1","interCustNo":"","prdSeries":"","prdCode":"zyc6706","prdMinBala":"0.00","bfirsCode":"","spvCode":"","assetpoolCode":"","clientMinRate":"0.00000","prdName":"zyc6702模板","prdMaxBala":"0.00","clientMaxRate":"0.00000","redDays":"0","managerType":"","divDays":"0","clientAvgRate":"0.00000","trusteeDuties":"","clientTypeArr":[],"ipoStartDate":"","rhCreditOrgTypeArr":[],"saleChannelArr":[],"interestBrand":"","rhCreditTypeArr":[],"openMode":"","ipoEndDate":"","onBusinessTime":[],"estabDate":"","cooperation":"","openPeriod":"","allotShareRate":"0.00000000","modeType":"","redeemShareRate":"0.00000000","theoryEndDate":"","endDate":"","otheropenDay":"","jiancangPeriod":"0","capitalSafeFlag":"","openIrregular":"","pfirstAmt":"0.00","ofirstAmt":"0.00","payBasis":"","incomeBzflag":"","firstopenBdate":"","psubUnit":"0.00","guestRate":"0.00000","collectShare":"0.00000","fundAccCode":"","openHoliFlag":"","openNumbers":"0.00","osubUnit":"0.00","fundAccName":"","collectAmt":"0.00","reportFlag":"01","pminHold":"0.000","openBusiness":"","navDigit":"4","openBusinessDes":"","ominHold":"0.000","structFlag":"","navRule":"0","structType":"","incomeRightTransferFlag":"","zzsbMemo":"","modelFlag":"02","status":"","templateCode":"1307","dataStatus":"3","feeinfodata":[]}
    # print(type(payloadData))
    with open('..\data\prdcode', 'w') as f:
        f.write('zycA'+time.strftime('%Y%m%d%H%M%S'))
    with open('..\data\prdcode', 'r') as b:
        return b.read()

# if __name__ == '__main__':
#     getNowtime()
#     print(getNowtime())
#     print(type(getNowtime()))
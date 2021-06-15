#author:钟怡成
import sys
sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\InterfaceTesting\env\Lib\site-packages")
import requests
import json

#将参数以字典的类型处理
r = requests.get('https://cart.taobao.com/trail_mini_cart.htm',params={'callback':'MiniCart.setData','t':'1526048972328'})
print('请求的url为：\n{0}'.format(r.url))

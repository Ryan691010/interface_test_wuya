#author:钟怡成

import sys
sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\InterfaceTesting\env\Lib\site-packages")
import requests

r = requests.get('http://cart.taobao.com/trail_mini_cart.htm')
print('HTTP协议返回的状态吗：\n{0}'.format(r.status_code))
print('返回Headers信息：\n{0}'.format(r.headers))
print('返回的cookies信息为：\n{0}'.format(r.cookies))
print('返回的响应数据内容：\n{0}'.format(r.text))

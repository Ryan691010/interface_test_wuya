import sys
sys.path.append(r"C:\Users\zhongyc27701\PycharmProjects\InterfaceTesting\env\Lib\site-packages")
import requests
import json

def getUrl():
    return 'http://10.20.155.135:8088/'
#登录的参数是form data格式，用一个字典封装
def loginData():
    dict1 = {
        'operator_code': 'zyc',
        'password': 'zyc111111=='
    }
    return dict1

def getToken():
    '''登录系统'''
    r=requests.post(
        url = getUrl()+'g/hsxone.omc/v/submitLogin',
        data = loginData()   #将用户名密码用字典传入data而且不用加上headers
        )
    # print(getUrl()+'g/hsxone.omc/v/submitLogin')
    # print(json.dumps(r.json(),indent=True))
    # print(r.status_code)
    # # print(r.json()['code'])
    # print(r.json()["data"][0]["user_token"])
    with open('token','w') as f:
        f.write(r.json()["data"][0]["user_token"])
    # self.assertEqual(r.json()['code'],20)
    # self.assertEqual(r.status_code,200)
    '''读取token文件内容'''
    with open('token','r') as f:
        # print(f.read())
        return f.read()

def getHeaders():
    headers = {
        # 'Token' : 'cbab5d44-90b9-46a2-acb4-065c89f628081',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'token='+getToken(),
        # 'Cookie': 'token=cbab5d44-90b9-46a2-acb4-065c89f628081',
        # 'Cookie': '4224396428EA776CBF0C71FAFA3938BFC8DC4F3946053C427CF7A5BC5B89DFA2F279F1E84CB8307D4B780806F262F0202E49397A8D8C82D8D6CE6D94735C079AE2A5641CC8D2077835F9954664545A6F',
        'Referer': 'http://10.20.155.135:8088/bfam6/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    return headers


def download(filepath):
    data = {"serialNo" : "1173196448339067904"}
    r = requests.get(
        url = getUrl()+'disclosure/dwnFile?serialNo=1173196448339067904',
        json = data,
        headers = getHeaders(),
        # stream=True
    )
    # print (r.text)
    # print(type(r.text))
    filestream = json.loads(r.text)["data"]["dwnResult"]
    # str转化成bytes
    bfilestream =bytes(filestream, encoding = "utf8")
    # print(type(filestream))
    # print(type(r.json()))
    # filestream = r.content["data"]["dwnResult"]
    # print ('文件流为：'+filestream)
    # print(r.content)
    # 判断请求是否成功，如果成功，就把数据写入到指定的文件中
    #python无法读取stream数据，只能读取二进制数据。这个方法失败
    if r.status_code == 200:
        #requests模块要用二进制的方法把数据写入到文件中。
        with open (filepath,'wb') as f :
            f.write(bfilestream)
        return print('下载文件成功')

if __name__ == '__main__':
    download(r'C:\Users\zhongyc27701\PycharmProjects\interface_test_wuya\wuya.doc')
from ddt import ddt, file_data
import yaml
import os
import json


def getUrl():
    if not os.path.isfile('../data/user.yaml'):
        raise FileNotFoundError("文件路径不存在， 请检查路劲是否正确： %s" % '../data/user.yaml')
    # open 方法打开直接读出来
    with open('../data/user.yaml', 'r', encoding='utf-8') as f:
        cfg = f.read()
    # print(cfg)
    # print(type(cfg))
    # 将其转化为字典形式
    d = yaml.load(cfg)
    # print(d)
    # print(type(d))
    # print(d['dict'])
    # print(type(d['dict']))
    # print(d['url'])
    # print(type(d['url']))
    # print("读取的测试文件数据： %s" %d)
    return d['url']


def getDit():
    if not os.path.isfile('../data/user.yaml'):
        raise FileNotFoundError("文件路径不存在， 请检查路劲是否正确： %s" % '../data/user.yaml')
    # open 方法打开直接读出来
    with open('../data/user.yaml', 'r', encoding='utf-8') as f:
        cfg = f.read()
    # print(cfg)
    # print(type(cfg))
    # 将其转化为字典形式
    d = yaml.load(cfg)
    # print(d)
    # print(type(d))
    # print(d['dict'])
    # print(type(d['dict']))
    # print(d['url'])
    # print(type(d['url']))
    # print("读取的测试文件数据： %s" %d)
    return d['dict']

# if __name__ == '__main__':
#     getUrl()

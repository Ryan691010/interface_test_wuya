'''读取token文件内容'''


def getToken():
    with open('../data/token', 'r') as f:
        return f.read()
#
# if __name__ == '__main__':
#
#     print(getToken())

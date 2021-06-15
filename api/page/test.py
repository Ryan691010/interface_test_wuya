# import os
# import xlrd
# from api.page.getToken import getToken
# from api.page.getNowtime import getNowtime
#
#
# def base_dir(filePath, folder='data'):
#     '''
#     返回一个这个文件在data目录的绝对路劲
#     :param filePath: 文件名称
#     :param folder: 文件夹
#     :return:
#     '''
#     return os.path.join(
#         os.path.dirname(
#             os.path.dirname(__file__)),
#         folder, filePath
#     )
#
#
# def readExcel(rowx, filePath='test_case_data.xls'):
#     '''
#     读取Excel文件中第rowx（索引）行的数据并且返回
#     :param rowx: 在Excel文件中的第rowx（索引）行
#     :param filePath: 文件名
#     :return:
#     '''
#     # 打开excel用例文件；
#     file = xlrd.open_workbook(base_dir(filePath))
#     # print(file)
#     sheet = file.sheet_by_name('Sheet1')
#     return sheet.row_values(rowx)
#
#
# def geturl(rowx):
#     '''
#     获取第rowx行的url
#     :param rowx: 行数
#     :return:
#     '''
#     return readExcel(rowx)[2]
#
#
# def getheaders(rowx):
#     '''
#     获取第rowx行的url
#     :param rowx: 行数
#     :return:
#     '''
#     return eval(readExcel(rowx)[3])
#
#
# def getpaylodData(rowx):
#     '''
#     获取第rowx行的url
#     :param rowx: 行数
#     :return:
#     '''
#     return eval(readExcel(rowx)[4])
#
# if __name__ == '__main__':
#     print(geturl(1))
#     print((type(geturl(1))))
#     print(getheaders(1))
#     print((type(getheaders(1))))
#     print(getpaylodData(1))
#     print((type(getpaylodData(1))))


import sys
print(sys.path)
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
# print(curPath)
# print(os.path.split(curPath))
# print(rootPath)
['C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\api\\page', 'C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya', 'C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 'C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 'C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39', 'C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\venv', 'C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\venv\\lib\\site-packages']
sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\api\\page')
sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\DLLs')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\lib')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39')
sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\venv')
sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\venv\\lib\\site-packages')



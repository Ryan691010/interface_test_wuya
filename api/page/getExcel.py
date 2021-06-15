import os
import xlrd
import json
from api.page.getToken import getToken
from api.page.getNowtime import getNowtime

class GetExcel():
    '''公共方法，获取Excel里的内容'''
    def base_dir(self,filePath,folder='data'):
        '''
        返回一个这个文件在data目录的绝对路劲
        :param filePath: 文件名称
        :param folder: 文件夹
        :return:
        '''
        return os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)),
            folder,filePath
            )

    def readExcel(self,rowx,filePath='test_case_data.xls'):
        '''
        读取Excel文件中第rowx（索引）行的数据并且返回
        :param rowx: 在Excel文件中的第rowx（索引）行
        :param filePath: 文件名
        :return:
        '''
        # 打开excel用例文件；
        file = xlrd.open_workbook(self.base_dir(filePath))
        # print(file)
        sheet = file.sheet_by_name('Sheet1')
        return sheet.row_values(rowx)

    def geturl(self,rowx):
        '''
        获取第rowx行的url
        :param rowx: 行数
        :return:
        '''
        return self.readExcel(rowx)[2]

    def getheaders(self,rowx):
        '''
        获取第rowx行的url
        :param rowx: 行数
        :return:
        '''
        return eval(self.readExcel(rowx)[3])

    def getpaylodData(self,rowx):
        '''
        获取第rowx行的url
        :param rowx: 行数
        :return:
        '''
        return eval(self.readExcel(rowx)[4])
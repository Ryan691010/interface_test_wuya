#author : 钟怡成
import sys

sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\api\\page')
sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\DLLs')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39\\lib')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\Programs\\Python\\Python39')
sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\venv')
sys.path.append('C:\\Users\\zhongyc27701\\PycharmProjects\\interface_test_wuya\\venv\\lib\\site-packages')
sys.path.append('C:\\Users\\zhongyc27701\\AppData\\Local\\JetBrains\\PyCharmCE2021.1\\python_stubs\\-106305771\\cx_Oracle')

import os.path
import unittest
import  HTMLTestRunner
from api.page.getNowtime import getNowtime
from api.testCase.test_user import TestUserApi
from api.testCase.test_prdTemplate import TestPrdApi
from xmlrunner import xmlrunner

# def allTestCases():
#     '''获取所有的测试模块'''
#     suite = unittest.defaultTestLoader.discover(
#         start_dir=r'C:\Users\zhongyc27701\PycharmProjects\interface_test_wuya\api\testCase',
#         pattern='test_*.py',
#         top_level_dir=None
#     )
#     return suite

def allTestCases():
    #现把TestCase的测试类按组分别导出所有的小案例
    user_tests = unittest.TestLoader().loadTestsFromTestCase(TestUserApi)
    prd_tests = unittest.TestLoader().loadTestsFromTestCase(TestPrdApi)
    #把所有小案例传到下面的smoke_tests组成一个suit集合
    smoke_tests = unittest.TestSuite([user_tests,prd_tests])
    # return print(smoke_tests)
    return smoke_tests

def run():
    #生成html格式的测试报告
    # fp = open(os.path.join(os.path.dirname(__file__),
    #                        '../report', getNowtime() + 'report.html')
    #           ,'w',encoding='utf-8')
    # HTMLTestRunner.HTMLTestRunner(
    #         stream=fp,
    #         title='接口自动化测试报告',
    #         description='基于python语言的接口自动化测试',
    #     ).run(allTestCases())
    # 生成xml格式的测试报告
    xmlrunner.XMLTestRunner(verbosity=2, output='../test-reports').run(allTestCases())


if __name__ == '__main__':
    run()
    # allTestCases()
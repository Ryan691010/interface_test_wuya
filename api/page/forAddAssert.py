# import sys
# sys.path.append(r"C:\Users\zhongyc27701\AppData\Local\Programs\Python\Python39\Lib\site-packages")
import cx_Oracle
# import sys
# print(sys.path)
def getAddnumber():
    with open('..\data\prdcode','r') as f:
        prd_code = f.read()
    #连接数据库，下面括号里内容根据自己实际情况填写
    # conn = cx_Oracle.connect('bfam6_zyc/bfam6_zyc:@10.20.37.119/orcl')
    conn = cx_Oracle.connect('bfam6_zyc/bfam6_zyc@10.20.37.119/orcl')
    # 使用cursor()方法获取操作游标
    # print('''Select * from ts_prdinfo where inter_prd_code="{0}{1}";'''.format('C1_',prd_code))

    cursor = conn.cursor()
    #使用execute方法执行SQL语句
    result=cursor.execute("Select * from ts_prdinfo where inter_prd_code='{0}{1}'".format('C1_',prd_code))
    #使用fetchone()方法获取一条数据
    data=cursor.fetchall()
    numbers = len(data)

    #获取所有数据
    # all_data=cursor.fetchall()

    #获取部分数据，8条
    #many_data=cursor.fetchmany(8)

    # print (data)
    conn.close()
    return numbers


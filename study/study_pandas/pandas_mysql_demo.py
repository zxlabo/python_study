import pandas as pd
from sqlalchemy import create_engine
from pandas import DataFrame
from pandasql import sqldf

user_name = 'root'
password = '899036c045'
host = '120.26.130.180:3306'
database_name = 'gyj_pontus'
charset = 'utf8mb4'
engine = create_engine(
    "mysql+pymysql://{}:{}@{}/{}?charset={}".format(user_name, password, host, database_name, charset))
con = engine.connect()  # 创建连接


# 查询操作
def query():
    sql_query = "select * from a"
    result = pd.read_sql_query(sql_query, con=con)
    print(result)


# 删除插入更新操作没有返回值，程序会抛出SourceCodeCloseError，并终止程序。如果想继续运行，可以try捕捉此异常。
def insert():
    # 插入操作
    sql_insert_business = "INSERT INTO a (id,`name`,age) VALUES(%d,%s,%d)" % (12, '22', 22)
    try:
        pd.read_sql_query(sql_insert_business, con=con)
    except Exception as e:
        print(e)


# 更新操作
def update():
    sql_update = "UPDATE a SET age=%d WHERE age=%d" % (66, 33)
    try:
        pd.read_sql_query(sql_update, con=con)
    except Exception as e:
        print(e)


# 删除操作
def delete():
    sql_delete = "DELETE FROM a WHERE age=%d" % 22
    try:
        pd.read_sql(sql_delete, con=con)
    except Exception as e:
        print(e)


# 查询数据返回的是DataFrame类型，可以保存到csv文件
def save_to_csv():
    data1 = {'name': ['xz', 'xc', 'xv'], 'age': [11, 22, 33]}
    df1 = DataFrame(data1)
    # index=False 不储存index
    df1.to_csv('student.csv', index=False)


'''
把DataFrame类型，可以保存到数据库
if_exists：表如果存在怎么处理：append：追加，replace：删除原表，建立新表再添加，fail：什么都不干
index=False：不插入索引index
输入中文会报错：sqlalchemy.exc.InternalError: (pymysql.err.InternalError) (1366, "Incorrect string value:）
解决：需要在create_engine的时候，设置charset='utf8mb4'，并且数据库对应的字段也要设置字符集utf8mb4，排序规则：utf8mb4_general_ci
'''


def save_mysql():
    data2 = {'name': ['北京', 'sh', 'hz'], 'age': [2111, 2012, 2122]}
    df2 = DataFrame(data=data2)
    df2.to_sql(name='a', con=con, if_exists='append', index=False)


'''
通过sql语句操作DataFrame,用SQL方式打开pandas，这里使用pandasql
'''


def query_repeat_trans():
    global table_name
    data3 = {'name': ['北京', 'sh', 'hz'], 'age': [2111, 2012, 2122]}
    table_name = DataFrame(data3)
    pysqldf = lambda sql: sqldf(sql, globals())
    sql = "select * from table_name where name ='北京'"
    print(pysqldf(sql))


query_repeat_trans()

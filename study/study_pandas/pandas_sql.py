'''
用SQL方式打开pandas，这里使用pandasql
pandasql中的主要韩式书sqldf，它接收两个参数：一个SQL查询语句，还有一组环境变量globals()或locals().
'''
import pandas as pd
from pandas import DataFrame
from pandasql import sqldf, load_meat, load_births

df1 = DataFrame({'name': ['zhangfei', 'xiaoming', 'a', 'b', 'c'], 'data': range(5, 10)})
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name='a' "
print(pysqldf(sql))
'''
lambda是用来做什么的呢
用来定义一个匿名函数，具体的使用形式为：
lambda argument_list:expression
argument_list:是参数列表
expression：是关于参数的表达式
'''

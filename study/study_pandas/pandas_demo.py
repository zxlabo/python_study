# -*- coding: utf-8 -*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

'''
pandas有两个核心的数据结构，基于这两种数据结构，Pandas可以对数据进行
导入、清洗、处理、统计、输出
Series：一维的序列
DataFrame：二维的表结构
'''
# x1 = Series([1, 2, 3, 4])
# x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(x1)
# d = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
# x3 = Series(d)
# print(x3)
# print("--------------------")
# data = {'Chinese': [11, 22, 33, 44, 55], 'English': [12, 34, 45, 67, 89], 'Math': [99, 88, 89, 98, 78]}
# df1 = DataFrame(data)
# print(df1)
# df2 = DataFrame(data, index=['A', 'B', 'C', 'D', 'E'], columns=['English', 'Chinese', 'Math'])
# print(df2)
# print("--------------------")
data = {'Chinese': [66, 95, 93, 90, 80], 'English': [None, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df3 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
'''
数据清洗
1.删除DataFrame中不必要的行或列【drop()函数】
2.对列名进行重命名，rename函数
3.去除重复的值 drop_duplicates
4.更改数据格式  使用astype来规范数据格式
5.删除数据间的空格或者字符 strip（删除左右空格） lstrip、rstrip
6.大小写转换 使用upper、lower、title[首字母大写]
7.查找空值 isnull
'''
# 删除语文这一列
df4 = df3.drop(columns=['Chinese'])
# print(df4)
# 删除张飞这一列
df5 = df3.drop(index=['ZhangFei'])
# print(df5)
# 把english改成英语
df3.rename(columns={'English': 'yingyu'}, inplace=True)
# print(df3)
df6 = df3.drop_duplicates()
# print(df6)
# df3['Chinese'].astype(np.int64)
df3['Chinese'].astype('str')
# 要在前面添加astype('str')，否则会报错
df3['Chinese'] = df3['Chinese'].astype('str').map(str.strip)
df3['Chinese'] = df3['Chinese'].astype('str').str.strip('$')
# df3.columns = df3.columns.str.upper()
# print(df3.isnull())
print(df3.isnull().any())
'''
使用apply函数对数据进行清洗
1.我们可以定义一个函数，在apply中使用
'''


def double_df(x):
    return 2 * int(x)


print(df3)
df3['Chinese'] = df3['Chinese'].apply(double_df)
print(df3)

'''
我们可以定义更复杂的函数
对DataFrame我们新增两列，new1是语文英语之和m倍，new2是和的n倍
axis=0:表示以行为轴进行操作
axis=1:表示以列为轴进行操作
'''
data = {'Chinese': [66, 95, 93, 90, 80], 'English': [90, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df8 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])


def plus(df, n, m):
    df['new1'] = (df['Chinese'] + df['English']) * 2
    return df


df9 = df8.apply(plus, axis=1, args=(2, 3))
print(df9)

'''
数据清洗之后，我们要对数据进行统计，describe函数
'''
print('数据清洗之后，我们要对数据进行统计，describe函数')
print(df8.describe())
print(df8['Chinese'].describe())
print(df8['Chinese'].mean())

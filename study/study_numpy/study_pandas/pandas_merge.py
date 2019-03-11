import pandas as pd
from pandas import Series, DataFrame

'''
数据表的合并 merge函数
1.基于指定列进行连接
2.inner内连接，也就是键的交集。相同的键是name，所以基于name进行内连接
3.left 左连接，以第一个df为主，第二个作为补充
4.right 右连接 以第二个为主
5.outer 外链接，相当于求两个df的并集
'''
df1 = DataFrame({'name': ['zhangfei', 'guanyu', 'a', 'b', 'c'], 'data1': range(5, 10)})
df2 = DataFrame({'name': ['zhangfei', 'guanyu', 'A', 'B', 'C'], 'data1': range(5, 10)})
# print(df1)
# print(df2)
# 基于指定列进行合并
# df3 = pd.merge(df1, df2, on='name')
# 2.inner内连接，也就是键的交集。相同的键是name，所以基于name进行内连接
# df3 = pd.merge(df1, df2, how='inner')
# 3.left 左连接，以第一个df为主，第二个作为补充
# df3 = pd.merge(df1, df2, how='left')
# df3 = pd.merge(df1, df2, how='right')
df3 = pd.merge(df1, df2, how='outer')
print(df3)


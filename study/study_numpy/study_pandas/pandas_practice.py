# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame

data = {'chinese': [66, 95, 95, 90, 80, 80], 'english': [65, 85, 92, 88, 90, 90], 'math': [None, 98, 96, 77, 90, 90]}
df1 = DataFrame(data, index=['张飞', '关羽', '赵云', '黄忠', '典韦', '典韦'], columns=['english', 'math', 'chinese'])
# 去除重复行
df1 = df1.drop_duplicates()
# 列名重新排序  axis=1表示已列为轴进行排序
cols = ['chinese', 'english', 'math']
df1 = df1.filter(cols, axis=1)
# 列名改为中文
df1.rename(columns={'english': '英语', 'math': '数学', 'chinese': '语文'}, inplace=True)


# 求成绩的总和，用apply函数
def total_score(df):
    df['总分'] = df['语文'] + df['数学'] + df['英语']
    return df


df1 = df1.apply(total_score, axis=1)
# 使用数学成绩均值，填充张飞同学的缺失值
df1['数学'].fillna(df1['数学'].mean(), inplace=True)
df1 = df1.apply(total_score, axis=1)
df1.sort_values(['总分'], ascending=[False], inplace=True)
print(df1)
print(df1.isnull().sum())
print(df1.describe())

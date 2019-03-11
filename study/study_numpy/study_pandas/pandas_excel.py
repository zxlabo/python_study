# 数据导入和输出
# pandas允许直接从xlsx、csv等文件导入数据，也可以输出到xlsx、csv等文件，非常方便
import pandas as pd
from pandas import Series, DataFrame

score = DataFrame(pd.read_excel('data.xlsx'))
score.to_excel("data1.xlsx")
print(score)

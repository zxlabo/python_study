'''
scikit-learn是python重要的机器学习库，现在我们学校如何使用scikit-learn进行数据规范化
'''

'''
Min-max规范化
让原始数据投射到指定空间[min,max],sk中有个指定函数MinMaxScaler
默认情况下是[0,1]
'''
from sklearn import preprocessing
import numpy as np

# 初始化数据
x = np.array([[0., -3., 1.], [3., 1., 2.], [0., 1., -1.]])
print(x)
# 将数据进行[0,1]规范化
min_max_scaler = preprocessing.MinMaxScaler()
min_max_x = min_max_scaler.fit_transform(x)
print(min_max_x)

'''
Z-score规范化
结果：将每行每列的值减去平均值，再除以方差，数值符合均值为0，方差为1的正态分布
'''
scaled_x = preprocessing.scale(x)
print(scaled_x)

'''
小数定标规范化
'''
j = np.ceil(np.log10(np.max(abs(x))))
decimal_x = x / (10 ** j)
print(decimal_x)

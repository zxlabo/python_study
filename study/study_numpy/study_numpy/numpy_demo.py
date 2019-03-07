# -*- coding: utf-8 -*-
import numpy as np

# shape 获得数组的大小  dtype获得元素的属性
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.shape)
print(a.dtype)

# dtype定义结构类型
# 定义数组的时候，用array指定结构数组的类型dtype=persontype
# peoples[:]['age'] 标识
# np.mean  计算平均值
persontype = np.dtype({'names': ['name', 'age', 'chinese', 'english', 'math'], 'formats': ['S32', 'i', 'f', 'f', 'f']})
peoples = np.array([('xiaoming', '23', '18.6', '80.5', '93'), ('LNGING', '23', '18.6', '80.5', '93'),
                    ('DAMING', '23', '18.6', '80.5', '93')], dtype=persontype)
print(peoples)
print(peoples[:]['age'])
print(np.mean(peoples[:]['age']))

# 连续数组的创建
# arange或linspace 都是创建等差数组
# arange 类似内置函数 range(),指定初始值、终值、步长
# linspace:linear space 线性等分向量，指定初始值、终值、元素个数
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)

# NumPy的算术运算
# 加、减、乘、除、求n次方、取余数
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))

# NumPy的统计函数
# 最大值、最小值、最大值与最小值的差、平均值、方差、标准差、是否符合正态分布
print('NumPy的统计函数 最大值、最小值、平均值、方差、标准差、是否符合正态分布')
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amax(c))
print(np.amin(c))
print(np.ptp(c))
# 统计数组的百分数 p的取值范围是0-100，
# 如果p=0：求最小值，p=50:平均值；p=100：最大值
print('统计数组的百分数 p的取值范围是0-100')
print(np.percentile(c, 0))
print(np.percentile(c, 50))
print(np.percentile(c, 100))
# 统计数组的中位数 median、平均数 mean
print('统计数组的中位数 median、平均数 mean')
print(np.median(c))
print(np.mean(c))
# 统计数组的加权平均值 average()
d = np.array([1, 2, 3, 4])
print('统计数组的加权平均值 average()')
print(np.average(d))
# 设置权重
wts = np.array([1, 2, 3, 4])
print(np.average(d, weights=wts))
# 上公式=（1*1+2*2+3*3+4*4）/（1+2+3+4）
# 统计数组中的标准差std()、方差var()
print('统计数组中的标准差std()、方差var()')
print(np.std(d))
print(np.var(d))
# NumPy排序
# 使用sort函数 sort(a,axis=-1,kind='quicksort',order=None)
# kind指定quicksort(快速排序)、mergesort(合并排序)、heapsort(堆排序)
# axis=-1:表示沿着数组的最后一个轴进行排序;
# axis=None:表示 采用扁平化的方式作为一个向量进行排序
# order:表示对于结构化的数组可以指定按照某个字段进行排序
print('NumPy排序')
e = np.array([[4994, 34, 64], [564, 6497, 994]])
print(np.sort(e))
print(np.amax(c, 0))
print(np.amax(c, 1))

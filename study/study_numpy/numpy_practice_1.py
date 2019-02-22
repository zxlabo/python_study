# -*- coding: utf-8 -*-
import numpy as np

'''
假设一个团队里有5名学员，成绩如下表所示。
1.用NumPy统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
2.总成绩排序，得出名次进行成绩输出。
'''
persontype = np.dtype({'names': ['name', 'chinese', 'english', 'math'], 'formats': ['S32', 'i', 'i', 'i']})
peoples = np.array(
    [("ZhangFei", 66, 65, 30), ("GuanYu", 95, 85, 98), ("ZhaoYun", 93, 92, 96), ("HuangZhong", 90, 88, 77),
     ("DianWei", 80, 90, 90)], dtype=persontype)
print("5名学员成绩分布")
print(peoples)

def bb():
    return 22, 33

def aa():
    cc, dd = bb()
    print(cc)
    print(dd)


aa()






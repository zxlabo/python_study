# -*- coding: utf-8 -*-
import numpy as np

'''
假设一个团队里有5名学员，成绩如下表所示。
1.用NumPy统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
2.总成绩排序，得出名次进行成绩输出。
'''


def show(project_name, project_scorts):
    print(project_name + "|" + str(np.mean(project_scorts)) + "|" + str(np.amin(project_scorts)) + "|" + str(
        np.amax(project_scorts)) + "|" + str(np.var(project_scorts)) + "|" + str(np.std(project_scorts)))


persontype = np.dtype(
    {'names': ['name', 'chinese', 'english', 'math', 'total'], 'formats': ['S32', 'i', 'i', 'i', 'i']})
peoples = np.array(
    [("ZhangFei", 66, 65, 30, 0), ("GuanYu", 95, 85, 98, 0), ("ZhaoYun", 93, 92, 96, 0), ("HuangZhong", 90, 88, 77, 0),
     ("DianWei", 80, 90, 90, 0)], dtype=persontype)
chinese_peoples = peoples[:]['chinese']
english_peoples = peoples[:]['english']
math_peoples = peoples[:]['math']
peoples[:]['total'] = chinese_peoples + english_peoples + math_peoples
print("5名学员成绩分布")
print(peoples)
print('科目|平均成绩|最小成绩|最大成绩|方差|标准差')
show('语文', chinese_peoples)
show('数学', math_peoples)
show('英语', english_peoples)
print("排名")
print(np.sort(peoples, order='total'))

'''
数据挖掘中，有几个核心的问题
1.如何选择各种分类器，选择哪个分类算法
2.如何优化分类器的参数，以便得到更好的分类准确率
3。数据探索
4.数据可视化
这个练习围绕以下目标
1.创建各类分类器，包括：SVM、决策树、KNN分类器、随机森林分类器
2.掌握GridSearchCv工具，优化算法模型的参数
3.使用Pipeline管道机制进行流水线作业
4.数据准备：数据规范化、数据姜维

'''

'''
在做分类算法的时候，我们需要调节网络参数，目的是得到更好的分类结果。
python提供了一个很好用的工具GridSearchCV,是python的参数自动搜索模块，它会把
把所有的清空运行一遍，然后返回最优的参数
'''
# 引用GridSearchCV工具包，我们使用sklearn自带的IRIS数据集，采用随机森林进行分类
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris

rf = RandomForestClassifier()
parameters = {'n_estimators': range(1, 11)}
iris = load_iris()
# 使用GridSearchCV进行参数调优
clf = GridSearchCV(estimator=rf, param_grid=parameters)
# 对iris数据集进行分类
clf.fit(iris.data, iris.target)
print('最优分数：%.4lf' % clf.best_score_)
print('最优参数：', clf.best_params_)
# 结果说明：当我们采用随机森林作为分类器的时候，最优准确率是 0.9667
# 当 n_estimators=9 的时候，是最优参数，也就是随机森林一共有9个子决策树

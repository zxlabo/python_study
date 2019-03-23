'''
python有一种Pipeline管道机制,管道机制就是让我们把每一步都按顺序列下来，
从而创建Pipeline流水线作业
每一步都采用（'名称'，步骤）的方式来表示
'''

'''
我们采用Pipeline管道机制,用StandardScaler方法对数据规范化，用PCA方法对数据进行降维，用随机森林进行分类。
1.我们采用StandardScaler方法对数据规范化，即采用数据规范化为：
均值为0，方差为1的正态分布
2.我们采用PCA方法对数据进行降维
3.采用随机森林进行分类
'''
# 使用 RandomForest 对 IRIS 数据集进行分类
# 利用 GridSearchCV 寻找最优参数, 使用 Pipeline 进行流水作业
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

rf = RandomForestClassifier()
parameters = {"randomforestclassifier__n_estimators": range(1, 11)}
iris = load_iris()
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('randomforestclassifier', rf)
])
# 使用 GridSearchCV 进行参数调优
clf = GridSearchCV(estimator=pipeline, param_grid=parameters)
# 对 iris 数据集进行分类
clf.fit(iris.data, iris.target)
print(" 最优分数： %.4lf" % clf.best_score_)
print(" 最优参数：", clf.best_params_)

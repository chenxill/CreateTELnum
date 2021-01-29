#导包
import numpy as np
import matplotlib.pyplot as plt

#导入数据
from  sklearn import datasets
#加载鸢尾花数据集（3分）
iris=datasets.load_iris()
#截取样本的所有行，后两列
X=iris.data[0:,2:]
y=iris.target

#对数据进行可视化展示（2分）
#X【y==标签，列数】
plt.scatter(X[y==0,0],X[y==0,1],color="r")
plt.scatter(X[y==1,0],X[y==1,1],color="g")
plt.scatter(X[y==2,0],X[y==2,1],color="b")
plt.show()

#对数据进行切分为训练数据和测试数据（3分）
from sklearn.model_selection import train_test_split
#将0.3的数据作为测试数据
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=51)


#对数据进行归一化操作（可自由选择合适的类库）（3分）
from sklearn.preprocessing import StandardScaler
#生成归一化对象
std_scaler=StandardScaler()
#进行归一计算
std_scaler.fit(X_train)
#进行归一化操作
X_train_std=std_scaler.transform(X_train)
X_test_std=std_scaler.transform(X_test)

#选择合适的算法，进行数据训练（可自由选择合适的算法）（3分）
from sklearn.tree import DecisionTreeClassifier
#参数（max_depth：层数，criterion：算法entropy（信息熵），random_state：随机数种子）
d_tree=DecisionTreeClassifier(max_depth=3,criterion="entropy",random_state=31)
d_tree.fit(X_train_std,y_train)
#打印对于测试数据的预测成绩（3分）
print(d_tree.score(X_test_std,y_test))


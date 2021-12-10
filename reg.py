import numpy as np
import pandas as pd
import pydotplus
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import tree
import os


train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

print('Shape of training data :',train_data.shape)
print('Shape of testing data :',test_data.shape)


train_x = train_data.drop(columns=['corona_result'],axis=1)
train_y = train_data['corona_result']

test_x = test_data.drop(columns=['corona_result'],axis=1)
test_y = test_data['corona_result']

model = LogisticRegression()

model.fit(train_x,train_y)

print('Coefficient of model :', model.coef_)

print('Intercept of model',model.intercept_)

predict_train = model.predict(train_x)


accuracy_train = accuracy_score(train_y,predict_train)
print('accuracy_score on train dataset : ', accuracy_train)

predict_test = model.predict(test_x)


accuracy_test = accuracy_score(test_y,predict_test)
print('accuracy_score on test dataset : ', accuracy_test)

coef_lr = pd.DataFrame({'var' : test_x.columns,
                        'coef' : model.coef_.flatten()
                        })

index_sort =  np.abs(coef_lr['coef']).sort_values(ascending = False).index
coef_lr_sort = coef_lr.loc[index_sort,:]

plt.figure(figsize=(14,8))
x, y = coef_lr_sort['var'], coef_lr_sort['coef']
rects = plt.bar(x, y, color='dodgerblue')
plt.grid(linestyle="-.", axis='y', alpha=0.4)
plt.tight_layout()
y1 = y[ y > 0];x1 = x[y1.index]
for a,b in zip(x1,y1):
    plt.text(a ,b+0.02,'%.2f' %b, ha='center',va='bottom',fontsize=12)
y2 = y[ y < 0];x2 = x[y2.index]
for a,b in zip(x2,y2):
    plt.text(a ,b-0.02,'%.2f' %b, ha='center',va='bottom',fontsize=12)
plt.show()
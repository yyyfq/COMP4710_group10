
from tkinter import Image
import numpy as np
import pandas as pd
import pydotplus
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


model = tree.DecisionTreeClassifier(criterion='entropy')

model.fit(train_x,train_y)

f_name = [i for i in train_x]
c_name = ['negative', 'positive']

dot_tree = tree.export_graphviz(model, out_file='out.dot', feature_names=f_name, class_names=c_name, filled=True, rounded=True, special_characters=True)
os.system('dot out.dot -Tpng -o tree.png')

print('Depth of the Decision Tree :', model.get_depth())

predict_train = model.predict(train_x)
print('Target on train data',predict_train)

accuracy_train = accuracy_score(train_y,predict_train)
print('accuracy_score on train dataset : ', accuracy_train)

predict_test = model.predict(test_x)
print('Target on test data',predict_test)

accuracy_test = accuracy_score(test_y,predict_test)
print('accuracy_score on test dataset : ', accuracy_test)


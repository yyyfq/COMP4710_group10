
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

print('Shape of training data :',train_data.shape)
print('Shape of testing data :',test_data.shape)


train_x = train_data.drop(columns=['corona_result'],axis=1)
train_y = train_data['corona_result']

test_x = test_data.drop(columns=['corona_result'],axis=1)
test_y = test_data['corona_result']

model = GaussianNB()

model.fit(train_x,train_y)

predict_train = model.predict(train_x)
print('Target on train data',predict_train)

accuracy_train = accuracy_score(train_y,predict_train)
print('accuracy_score on train dataset : ', accuracy_train)

predict_test = model.predict(test_x)
print('Target on test data',predict_test)

accuracy_test = accuracy_score(test_y,predict_test)
print('accuracy_score on test dataset : ', accuracy_test)
import csv
import pandas as pd

testData = pd.read_csv('0083.csv', low_memory=False)
testDf = pd.DataFrame(testData)
print(testDf.__len__())
# testData = testData.drop(testData[(testData['cough']=='None') | (testData['fever']=='None') | (testData['corona_result']=='other')].index)
testData = testData.drop(testData[(testData['age_60_and_above']=='None') | (testData['cough']=='None') | (testData['fever']=='None') | (testData['gender']=='None') | (testData['corona_result']=='other')].index)
testData.dropna(axis=0, how='any', inplace=True)
testData['gender'] = testData['gender'].astype(str)
testData['gender'] = testData['gender'].apply(lambda x:x.replace("female","0"))
testData['gender'] = testData['gender'].apply(lambda y:y.replace("male","1"))
testData['age_60_and_above'] = testData['age_60_and_above'].apply(lambda m:m.replace("Yes","1"))
testData['age_60_and_above'] = testData['age_60_and_above'].apply(lambda n:n.replace("No","0"))
testData['corona_result'] = testData['corona_result'].apply(lambda p:p.replace("negative","0"))
testData['corona_result'] = testData['corona_result'].apply(lambda q:q.replace("positive","1"))
testData.drop(["test_indication","test_date"],axis=1,inplace=True)
# testData.drop(["test_indication","test_date","gender","age_60_and_above"],axis=1,inplace=True)
testData.to_csv('mytestdata.csv',index=False)
test1 = testData[0:2160000]
test2 = testData[2160000:]
test1.to_csv('train.csv',index=False)
test2.to_csv('test.csv',index=False)
print(test2)
# print(testData)
print(testData.head())
print(testData.__len__())
print(test1.__len__())
print(test2.__len__())

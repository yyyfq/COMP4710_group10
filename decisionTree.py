import pandas as pd

def createDataSet():
    data = pd.read_csv('dataset/testDataset.csv', header=0)

    return data
  

def splitDataSetTest(data,cough,fever,sore_throat,shortness_of_breath,head_ache,corona_result,age_60_and_above,gender):
    retDataSet1 = []
    df=None

    if (cough==1):
        df = data["cough"] == 1
    elif(fever==1):
        df = data["fever"] == 1
    elif (sore_throat == 1):
        df = data["sore_throat"] == 1
    elif (shortness_of_breath == 1):
        df = data["shortness_of_breath"] == 1
    elif (head_ache == 1):
        df = data["head_ache"] == 1
    elif (corona_result == 1):
        df = data["corona_result"] == 1
    elif (age_60_and_above == 1):
        df = data["age_60_and_above"] == 1
    elif (gender == 1):
        df = data["gender"] == 1

    filtered_df = data[df]
    retDataSet1.append(filtered_df)

    return retDataSet1

##### Introduction

At the end of 2019, the new coronavirus swept the world. As of November 12, 2021, there were over 251 million infection cases and 5.07 million deaths worldwide. This virus has mutated into various variants in countries like the United Kingdom, South Africa, the United States, India and Brazil.  These variants increase the severity of the disease and lead to faster transmission, higher mortality, and reduced vaccine effectiveness. Besides, the virus also challenges the global medical system, including the sharp increase in the demand for hospital beds. There is a severe shortage of medical equipment, and many medical staff have also been infected, showing the harm brought by the new coronavirus to the world.

According to the COVID-related issues published by the WHO, the primary way of transmission of the new coronavirus is respiratory droplet transmission and contact transmission. Common signs of people infected with the coronavirus include respiratory symptoms, fever, cough, tiredness, and loss of taste or smell. The infection can also lead to pneumonia, difficulty breathing or shortness of breath, loss of speech or mobility, confusion, chest pain, and even death in more severe cases. Although the World Health Organization stated that frequent hand washing, disinfection, social distancing, wearing a mask, and not touching the face could protect a person from infection, some people may unfortunately become one of the cases. Therefore, the anticipation and effective screening of different cases' conditions (such as age and gender) and their possible symptoms are crucial for reducing the burden on the healthcare system and medical staff. Machine learning classification algorithms and data sets have also become essential tools for designing COVID-19 prediction models.



##### Background and related work

Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.

Broadly, there are 3 types of Machine Learning Algorithms

1. Supervised Learning
   In supervised learning, the machine uses the label data of the input and output data, and determines the appropriate pattern classification to combine to complete the work. When the machine receives unknown data, he will judge which mode can be applied, and demonstrate the label data and classify the new data.
2. Unsupervised Learning
   Unsupervised learning uses unlabeled data. The goal of unsupervised learning is to master the shape of the data. It includes a process called "clustering", which divides a group of data with common characteristics together, or extracts association rules among them.
3. Reinforcement Learning:
   The machine learns from past experience and tries to capture the best possible knowledge to make accurate business decisions.

Regarding the related works for COVID-19 prediction, most of them are aimed at predicting the incidence of the virus and the effectiveness of the vaccine rather than the specific symptoms of the testers or positive patients. Therefore, the mining of COVID symptom data may not be as easy as imagined.

Regarding the existing available datasets, we plan to use classification algorithms in combination with the machine's autonomous learning technology to apply to the current research on the new coronavirus.

Data classification has two stages: the learning stage and the classification stage. The machine builds a classification model by analyzing the training data set with a classification algorithm, and then evaluates the accuracy of the classification rule by checking the data set. If the accuracy is acceptable, the rule can be used for new datasets.

The reason why we choose decision tree as our algorithm not only because the datasets contains all the symptom gender and age of the testers but also missing values in the data do not affect the process of building a decision tree to any considerable extent and a decision tree model is very intuitive and easy to explain to technical teams as well as stakeholders. Besides, the model we build aim to predict the possible complications of the new crown patient and do the rapid treatment to save more lives.

##### Reference

COVID-19 Explorer, https://worldhealthorg.shinyapps.io/covid/

What you need to know about the coronavirus variantshttps://www.washingtonpost.com/health/interactive/2021/01/25/covid-variants/

WHO Health topics Coronavirus disease (COVID-19),https://www.who.int/health-topics/coronavirus#tab=tab_3

Prediction of COVID-19 growth and trend using machine learning approach

[E. Gothai](https://www.ncbi.nlm.nih.gov/pubmed/?term=Gothai E[Author]&cauthor=true&cauthor_uid=33880331), [R. Thamilselvan](https://www.ncbi.nlm.nih.gov/pubmed/?term=Thamilselvan R[Author]&cauthor=true&cauthor_uid=33880331), [R.R. Rajalaxmi](https://www.ncbi.nlm.nih.gov/pubmed/?term=Rajalaxmi R[Author]&cauthor=true&cauthor_uid=33880331), [R.M. Sadana](https://www.ncbi.nlm.nih.gov/pubmed/?term=Sadana R[Author]&cauthor=true&cauthor_uid=33880331), [A. Ragavi](https://www.ncbi.nlm.nih.gov/pubmed/?term=Ragavi A[Author]&cauthor=true&cauthor_uid=33880331), and [R. Sakthivel](https://www.ncbi.nlm.nih.gov/pubmed/?term=Sakthivel R[Author]&cauthor=true&cauthor_uid=33880331)

Machine learning-based prediction of COVID-19 diagnosis based on symptoms

- [Yazeed Zoabi](https://www.nature.com/articles/s41746-020-00372-6#auth-Yazeed-Zoabi), [Shira Deri-Rozov](https://www.nature.com/articles/s41746-020-00372-6#auth-Shira-Deri_Rozov) & [Noam Shomron](
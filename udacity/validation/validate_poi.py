#!/usr/bin/python


import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )


features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
xtrain,xtest,ytrain,ytest=train_test_split(features,labels,test_size=0.3,random_state=42)
clf=tree.DecisionTreeClassifier()
clf.fit(xtrain,ytrain)
pred=clf.predict(xtest)
print(accuracy_score(pred,ytest))

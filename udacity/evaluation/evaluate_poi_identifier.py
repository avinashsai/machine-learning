#!/usr/bin/python




import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
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
n=len(pred)
#number of pois in the test data
print(sum(pred))
#number of people
print(n)
#accuracy of the dataset
print(ytest)
print(pred)
count=0
for i in range(0,n):
	if(pred[i]==0.0):
		count=count+1
print(count)
#number of true positives
count=0
for i in range(0,n):
	if(pred[i]==1 and ytest[i]==1):
		count+=1
print(count)
#precision score and recall score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
print(precision_score(pred,ytest))
print(recall_score(pred,ytest))
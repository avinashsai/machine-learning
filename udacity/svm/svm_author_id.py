#!/usr/bin/python

    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()





from sklearn import svm
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
clf=SVC(kernel="rbf",C=10000)
clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
target_names=['class 0','class 1']
print(classification_report(pred,labels_test,target_names=target_names))

#########################################################



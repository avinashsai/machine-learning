#!/usr/bin/python


    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf=GaussianNB()
clf.fit(features_train,labels_train)
t0 = time()
print "training time:", round(time()-t0, 3), "s"
pred=clf.predict(features_test)
t0 = time()
print "training time:", round(time()-t0, 3), "s"
accuracy=accuracy_score(pred,labels_test)
print(accuracy)
#########################################################



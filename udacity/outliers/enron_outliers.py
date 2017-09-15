#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

persons=[]
n=len(data_dict)
for i in range(0,n):
	a=data_dict.values()[i]
	key=data_dict.keys()[i]
	if(a['salary']!='NaN'):
		persons.append((key,int(a['salary'])))
 
persons=sorted(persons,key=lambda x:x[1],reverse=True)	
print(persons[0][0])

bandits=[]
for i in range(0,n):
	a=data_dict.values()[i]
	key=data_dict.keys()[i]
	if(a['salary']=='NaN'or a['bonus']=='NaN'):
		continue
	elif(int(a['salary'])>=1000000 and int(a['bonus'])>=5000000):
		bandits.append((key,int(a['salary'])))
print(bandits)

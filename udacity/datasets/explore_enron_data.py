

import pickle
import numpy as np
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


# find number of features in the data set
#print(enron_data)
#print(len(enron_data.keys()))

#find number of poi entries with value 1 in the dictionary

count=0
for i in range(0,len(enron_data)):
	s=enron_data.values()[i]
	if(s['poi']=='1'):
		count=count+1
print(count)

#find number of poi entries with values NaN
count=0
for i in range(0,len(enron_data)):
	s=enron_data.values()[i]
	if(s['poi']=='NaN'):
		count=count+1
print(count)
#poi entries in the names list
poi_data = open('../final_project/poi_names.txt','r')
fr=poi_data.readlines()
print(len(fr[2:]))

#print totalstock value of james presentise

print(enron_data["PRENTICE JAMES"]['total_stock_value'])

#noofemails from colwell wesley to poi
s=enron_data.keys()
for i in range(0,len(s)):
	if(s[i]=='COLWELL WESLEY'):
		a=enron_data.values()[i]
		print(a['from_this_person_to_poi'])


#stockoptions
[name for name in enron_data.keys() if "SKILLING" in name]
print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
#largest money
k1=(enron_data['SKILLING JEFFREY K']['total_payments'])
k2=(enron_data['FASTOW ANDREW S']['total_payments'])
k3=(enron_data['LAY KENNETH L']['total_payments'])
print(max(k1,k2,k3))


#print number os salary and email addresses having NaN
count1=0
count2=0
for i in range(0,len(enron_data.keys())):
	a=enron_data.values()[i]
	if(a['salary']!='NaN'):
		count1=count1+1
	if(a['email_address']!='NaN'):
		count2=count2+1
print(count1)
print(count2)

#percentage of people having total_payments as NaN

s=enron_data.keys()
n=len(s)
count1=0
for i in range(0,n):
	a=enron_data.values()[i]
	if(a['total_payments']=='NaN'):
		count1+=1
print(count1)
#percentage of poi having NaN

s=enron_data.keys()
n=len(s)
count1=0
for i in range(0,n):
	a=enron_data.values()[i]
	if(a['total_stock_value']=='NaN'):
		count1+=1
print(count1)
print(float (count1*100)/n)



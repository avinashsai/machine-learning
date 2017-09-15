#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    
    cleaned_data = []

    outiler_data=(predictions-net_worths)**2
    cleaned_data=zip(ages,net_worths,outiler_data)
    cleaned_data=sorted(cleaned_data,key=lambda x:x[2],reverse=True)
    n=len(cleaned_data)
    n=int(n*0.1)
    return cleaned_data[n:]; 

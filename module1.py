import random
import os
import shutil
import re
import string

#read
def read(mypath):
    empdata={} # This is a Dictionary
    for file in os.listdir(mypath):
        if file.endswith(".txt"):
            try:
                f2=open(f"{mypath}/{file}",'r')
            except:
                print("Unable to open file %s for reading. Skipping this file" % f"(mypath)/(file)" )
                continue				
            try:
                line=f2.readline()
            except:
                print("Unable to read from file. Skipping this file" % f"(mypath)/(file)" )
                continue				
            matches=re.findall(r"[1-9][0-9]*",line)
            empdata[matches[0]]=int(matches[1])
            f2.close()
    return empdata
#sort
def sorting(empdata):
    emplist=list(empdata.items())
    l=len(emplist)
    for i in range(l-1):
        for j in range(i+1,l):
            if emplist[i][0]>emplist[j][0]:
                t=emplist[i]
                emplist[i]=emplist[j]
                emplist[j]=t
    return emplist
#search
def search(arr, l, r, x):
    filtlist=[]	# This is a List
    while l <= r:
        mid = l + (r - l) // 2;
        if int(arr[mid][0]) == x:
            return arr[mid]
        elif int(arr[mid][0]) < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


#import random
#import os
#import shutil
#import re
#import string

import sys
sys.path.append('C:/Users/mahsh/OneDrive - Software AG/Desktop/Python')
from module1 import read, sorting, search
#from module1 import *

#main
if __name__=="__main__":
   
    empdata=read("./empdata")
    print(empdata)
    emplist=sorting(empdata)
   
    Empid=int(input("Enter Employee ID:"))
    selectedEmp = search(emplist, 0, len(emplist)-1, Empid)
    print(selectedEmp)

import random
import os
import shutil
import re
import string

import sys
sys.path.append('C:/Users/mahsh/OneDrive - Software AG/Desktop/Python')
import module1

#generation
def generate(mypath,N):
    errors = ("Unable to delete directory", "Unable to create directory", "Unable to create file", "Unable to write to file") # This is a tuple
    if(os.path.exists(mypath)):
        try:
            shutil.rmtree(mypath)
        except:
            print("%s: %s" % (errors[0], mypath)) 
            return
    try:
        os.mkdir(mypath)
    except:
        print("%s: %s" % (errors[1], mypath)) 
        return
    for i in range(N):
        empname=''.join(random.choices(string.ascii_lowercase, k = 7))
        empid=random.randint(1000000000,9999999999)
        empsal=random.randint(100000,99999999)
        try:
            f=open(f"{mypath}/{empname}.txt",'w')
        except:
            print("%s: %s" % (errors[2], mypath)) 
            continue
        try:
            f.write(f"This is employee record for {empid} for which {empsal} amount has been credited to his account.")
        except:
            print("%s: %s" % (errors[3], mypath)) 
            continue
        f.close()
if __name__=="__main__":
   
    generate("./empdata",10)
    empdata=module1.read("./empdata")
    print(empdata)


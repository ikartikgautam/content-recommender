#imports
import pandas as pd

#csv files read
art = pd.read_csv("artists.csv",header=None)
users = pd.read_csv("users.csv",header=None)

#variables
uId = ""
crr_user=-1
signup = 0
temp=pd.DataFrame({0:["uIdt"],1:[122],2:["cms"]}) 

#user login
print("Welcome !!\n")
uId = input("Enter the userid :")

for i in users[0]:
    if(uId==i):
        print("User Found")
        crr_user=i
        break

if(crr_user==-1):
    print("not Found !!")
    #create new account
    signup=int(input("Do you want to make new account?[1/0]"))
    print(signup)
    if (signup==1):
        temp=pd.DataFrame({0:[uId],1:[122],2:["cms"]}) 
        users=users.append(temp,ignore_index=True)
        print(users)       
else:
    print("user = ",crr_user)        

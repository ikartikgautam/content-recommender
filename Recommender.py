#imports
import pandas as pd

#csv files read
art = pd.read_csv("artists.csv",header=None)
users = pd.read_csv("users.csv",header=None)

#variables
uId = ""
crr_user=-1
signup = False

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
    signup=input("Do you want to make new account?[1/0]")
    if(signup==True):
        temp=pd.DataFrame({0:["uId"],1:[122],2:["cms"]}) 
        users=users.append(temp,ignore_index=True)
else:
    print("user = ",crr_user)        

print(users)    
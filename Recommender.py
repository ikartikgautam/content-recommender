#imports
import pandas as pd

#csv files read
art = pd.read_csv("artists.csv",header=None)
users = pd.read_csv("users.csv",header=None)

#variables
uId = ""
crr_user=-1
signup = 0

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
        bpm=int(input("Enter avg bpm"))
        artists=input("Enter the artists u like:")
        temp=pd.DataFrame({0:[uId],1:[bpm],2:[artists]}) 
        users=users.append(temp,ignore_index=True)
        users.to_csv("users.csv",index=False,header=False)
        print(users)       
else:
    print("user = ",crr_user)        

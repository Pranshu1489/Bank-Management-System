import os
import platform
import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host="localhost",\
user="root",\
password="123456",\
database="Bank")
mycursor=mydb.cursor()
def AccInsert():
    L=[]
    Accno=int(input("Enter the Account number : "))
    L.append(Accno)
    name=input("Enter the Customer Name: ")
    L.append(name)
    age=int(input("Enter Age of Customer : "))
    L.append(age)
    occup=input("Enter the Customer Occupation : ")
    L.append(occup)
    Address=input("Enter the Address of the Customer : ")
    L.append(Address)
    Mob=int(input("Enter the Mobile number : "))
    L.append(Mob)
    Aadharno=int(input("Enter the Aadhar number : "))
    L.append(Aadharno)
    Amt=float(input("Enter the Money Deposited : "))
    L.append(Amt)
    AccType=input("Enter the Account Type (Saving/RD/PPF/Current) : ")
    L.append(AccType)
    cust=(L)
    sql="Insert into ACCOUNT(Accno ,Name,Age,occu,Address,Mob,Aadharno,amt,AccType) values(%s,%s,%s, %s,%s,%s, %s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()

def AccView():
     print(" View All")
     sql="select * from account"
     mycursor.execute(sql)
     res=mycursor.fetchall()
     print("The Customer details are as follows : ")
     #print("(Accno ,Name,Age,occu,Address,Mob,Aadharno,amt,AccType)")
     #for x in res:
     k=pd.DataFrame(res,columns=['AccNo','Name','Age','Occu','Add','Mob','Aadh','Amt','AccTy'])
     print(k)
     #print(x)

def AccDeposit():
    L=[]
    Accno=int(input("Enter the Account number : "))
    L.append(Accno)
    Amtdeposite=eval(input("Enter the Amount to be deposited : "))
    L.append(Amtdeposite)
    month=input("Enter month of Salary : ")
    L.append(month)
    cust=(L)
    sql="Insert into amt(Accno,Amtdeposite,Month) values(%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()

def accView():
        print("Please enter the details to view the Money details :")
        Accno=int(input("Enter the Account number of the Customer whose amount is to be viewed : "))
        sql="Select Account.Accno, Account.Name, Account.Age,Account.occu,Account.Address,Account.Mob,Account.Aadharno,Account.Amt,Account.AccType, sum(amt.Amtdeposite), amt.month from Account INNER JOIN amt ON Account.Accno=amt.Accno and amt.Accno = %s"
        rl=(Accno,)
        mycursor.execute(sql,rl)
        res=mycursor.fetchall()
        for x in res:
            print(x)

def closeAcc():
               def abcd():
                              Accno=int(input("Enter the Account number of the Customer to be closed : "))
                              rl=(Accno)
                              sql="Delete from account where Accno=%s"
                              mycursor.execute(sql,rl)
                              print(Accno,"Suuccessfuly deleted")
                              mydb.commit()
               abcd()
def MenuSet():  
    print("Enter 1 : To Add Customer")
    print("Enter 2 : To Deposit Money   ")
    print("Enter 3 :To Close Account ")
    print("Enter 4 :To View Customer Details")
    print("Enter 5 :To View all Customers Details")
    try: 
        userInput = int(input("Please Select An Above Option: "))  
    except ValueError:
        exit("\nHy! That's Not A Number")  
    else:
        print("\n")  
    if(userInput == 1):
                   AccInsert()
    elif (userInput==2):
                   AccDeposit()
    elif (userInput==3):
                   closeAcc()
    elif (userInput==4):
                   accView()
    elif (userInput==5):
                   AccView()
    else:
        print("Enter correct choice. . . ")
    MenuSet()
def runAgain():
    runAgn = input("\nwant To Run Again Y/n: ")
    while(runAgn.lower() == 'y'):
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
    MenuSet()
    runAgn = input("\nwant To Run Again Y/n: ")
    runAgain()
MenuSet()

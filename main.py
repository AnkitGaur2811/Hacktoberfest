import pathlib as path
import pickle as pic
import os


class Account:
    Accountno=0
    Accholdername=""
    Deposit=0
    Acctype=""

    #creation of account
    def createAcc(self):
        self.Accountno=checkAccountno()
        self.Accholdername=input("Enter the name of Account holder:")
        self.Acctype=input("Enter the type of account you need( C for current : Enter S for saving:):")
        self.Deposit=int(input("enter the amount for deposite(>= 2000 for current >=500 for savings ) :"))
        if self.Acctype=="s" or self.Acctype=="S":
            while(self.Deposit<500):
                print ("please enter the correct amount this amount is not excepted it must be >=500" )
                self.Deposit=int(input("enter the amount for deposite(>= 2000 for current >=500 for savings ) :"))
                if(self.Deposit>500):
                    break
        else:
             while(self.Deposit<2000):
                print ("please enter the correct amount this amount is not excepted it must be >=2000" )
                self.Deposit=int(input("enter the amount for deposite(>= 2000 for current >=500 for savings ) :"))
                if(self.Deposit>2000):
                    break
        
        print("\n\t\t##congratulation! you are account is sucessfully created##")
    
    #showing created account
    def Showaccount(self):
        print("\n Account number: ",self.Accountno,"\n Account holder name:",self.Accholdername)
        if (self.Acctype=="s" or self.Acctype=="S"):
            print("Account type: savings")
        else:
            print("Account type: current")
        print("Deposited amount=",self.Deposit)
     
    #modification in data
    def modifydata(self):
           print("\n Account number: ",self.Accountno)
           self.Accholdername=input("Enter the modified name of holder:")
           self.Acctype=input("Enter the modified Account type:")
           print("#data modified#")
    
    def Depositamt(self,amount):
        self.Deposit+=amount
        
    def withdrawamt(self,amount):
        self.Deposit-=amount
        
    def aldata(self):
         print(self.Accountno," ",self.Accholdername," ",self.Acctype," ",self.Deposit)
         
    def getAccno(self):
        return self.Accountno
    
    def getAccholdername(self):
        return self.Accholdername
    
    def getAcctype(self):
        return self.Acctype
    
    def getDeposit(self):
        return self.Deposit

#check if account alredy exist or not
def checkAccountno():
    file=path.Path("Accounts.data")
    if not file.exists():
        Account=int(input("Enter the Accountno:"))
        return Account
    else:
        while(1):
            Account=int(input("Enter the Accountno:"))
            filein=open("Accounts.data","rb")
            mylist=pic.load(filein)
            filein.close()
            for item in mylist:
                if  (item.getAccno()==Account):
                    print("this account already exits plz enter again")
                else:
                    return Account
                
                    
    
#first view of bank
def intro():
    print("\t _____________________________________________ ") 
    print("\t|                                             |")
    print("\t|     Welcome to the Pseudo Currency Bank     |")
    print("\t|_____________________________________________|")  

#write the created account in file
def writeaccount():
    account=Account()
    account.createAcc()
    writeaccountinfile(account)
    
#diplay all bank accounts in bank
def displayall():
    file=path.Path("Accounts.data")
    if file.exists():
        filein=open("Accounts.data","rb")
        mylist=pic.load(filein)
        for item in mylist:
            print(item.Accountno," ",item.Accholdername," ",item.Acctype," ",item.Deposit)
        filein.close()
    else:
        print("No record to dislay at time")

#display a special account on demand
def displaysp(num):
    file=path.Path("Accounts.data")
    if file.exists():
        filein=open("Accounts.data","rb")
        mylist=pic.load(filein)
        filein.close()
        found=False
        for item in mylist:
            if item.Accountno==num:
                print("your account balance is Rs.",str(item.deposit))
                found=True
    else:
        print("No record to search")
    if not found:
        print("you might enter wrong no. this account doesn't exist")

#deposit and withdraw the amount in/ from account
def depositwithdraw(num1,num2):
    file=path.Path("Accounts.data")
    if file.exists():
        filein=open("Accounts.data","rb")
        mylist=pic.load(filein)
        filein.close()
        os.remove("Accounts.data")
        for item in mylist:
            if item.Accountno==num1:
                if num2==1:
                    amount=int(input("Enter the amount to be deposited:"))
                    item.Deposit+=amount
                    print("Your account is updated")
                elif num2==2:
                    amount=int(input("Enter the amount to be withdrawed:"))
                    if amount<=item.Deposit:
                        item.Deposit-=amount
                    else:
                        print("you cannot withdraw this much large amount")
    else:
        print("NO RECORDS!!")
    outfile=open("newaccounts.data","wb")
    pic.dump(mylist,outfile)
    outfile.close()
    os.rename("newaccounts.data","Accounts.data")
    
#delete the specific account
def delete(num):
    file=path.Path("Accounts.data")
    if file.exists():
        filein=open("Accounts.data","rb")
        oldlist=pic.load(filein)
        filein.close()
        newlist=[]
        for item in oldlist:
            if item.Accountno!=num:
                newlist.append(item)
        os.remove("Accounts.data")
        outfile=open("newaccounts.data","wb")
        pic.dump(newlist,oldlist)
        outfile.close()
        os.rename("newaccounts.data","Accounts.data")

#modify account 
def modifyacc(num):  
    file=path.Path("Accounts.data")
    if file.exists():
        filein=open("Accounts.data","rb")
        oldlist=pic.load(filein)
        filein.close()
        os.remove("Accounts.data")
        for item in oldlist:
            if item.Accountno==num:
                item.Accholdername=input("Enter the modified name of holder:")
                item.Acctype=input("Enter the modified Account type:")
                item.deposit=int(input("Enter the amount:"))
    outfile=open("newaccounts.data","wb")
    pic.dump(oldlist,outfile)
    outfile.close()
    os.rename("newaccounts.data","Accounts.data")


#writeing account in file
def writeaccountinfile(account):
    file=path.Path("Accounts.data")
    if file.exists():
        filein=open("Accounts.data","rb")
        oldlist=pic.load(filein)
        oldlist.append(account)
        filein.close()
        os.remove("Accounts.data") 
        
    else:
        oldlist=[account]
    
       
    outfile=open("newaccounts.data","wb")
    pic.dump(oldlist,outfile)
    outfile.close()
    os.rename("newaccounts.data","Accounts.data")
    
#__________________________________main________________________________________#

ch=""
num=0
intro()

while ch!=8:
    print("\t\t MAIN MENU")
    print("\t\t1.NEW ACCOUNT")
    print("\t\t2.DEPOSIT AMOUNT") 
    print("\t\t3.WITHDRAW AMOUNT")
    print("\t\t4.BALANCE ENQUIRY")
    print("\t\t5.ALL ACCOUNT HOLDERS")
    print("\t\t6.CLOSE AN ACCOUNT")
    print("\t\t7.MODIFY AN ACCOUNT")
    print("\t\t8.EXIT")
    print("\t\tSelect your option for action:")
    ch=input()
    
    
    if ch=="1":
        writeaccount()
    elif ch=="2":
        num=int(input("Enter the account no:"))
        depositwithdraw(num,1)
    elif ch=="3":
        num=int(input("Enter the account no:"))
        depositwithdraw(num,2)
    elif ch=="4":
        num=int(input("Enter the account no:"))
        displaysp(num)
    elif ch=="5":
        displayall()
    elif ch=="6":
        num=int(input("Enter the account no:"))
        delete(num)
    elif ch=="7":
        num=int(input("Enter the account no:"))
        modifyacc(num)
    elif ch=="8":
        print("Thanks for using our system")
        break  
    else:
        print("Invalid choice")
    
    
    
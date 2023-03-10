# -*- coding: utf-8 -*-
"""BankSystemproblems.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CA0vwO6VIuM1ysaP4zQ2u-dsVV8AXqi6
"""

class Bank:
  account_no=202200
  def create_account(self):
    Bank.account_no+=1
    self.accno=Bank.account_no
    print("Your account created: ",self.accno)
    self.name=input("Enter name: ")
    while True:
      self.amount=float(input("Enter amount to start account: "))
      if self.amount<2000:
        print('you need minimum 2000 to start a account \n please enter amount greater than 2000')
      else:
        break   
    print("Account number:"+str(self.accno)+" Name:"+self.name+" Amount:"+str(self.amount))
    #print(self)#self.deposit_ammount()
  def __str__(self):
    return "Account number:"+str(self.accno)+" Name:"+self.name+" Amount:"+str(self.amount)
  
  def deposit_ammount(self):
    while True:
      self.deposit=float(input("Enter amount to deposit: "))
      if self.deposit<=0:
        print('please enter amount greater than 0')
      else:
        self.amount +=self.deposit
        break 
  
  def withdraw_ammount(self):
    while True:
      self.withdraw=float(input("Enter amount to withdraw: "))
      amnt = self.amount-self.withdraw
      if self.withdraw<=0 or amnt<2000:
        print('Transaction will lead to minimum account hence terminated')
      else:
        self.amount = amnt
        break

b1=Bank()

b1.create_account()

b1.withdraw_ammount()

print(b1)

b1.deposit_ammount()

b2=Bank()
b2.create_account()

b1.deposit_ammount()

print(b1)

acclist=[]
while True:
  ch=int(input("\n1.Create Account\n2.Check Balance\n3.Deposit Amount\n4.Withdraw amount\n0.Exit\n:"))
  if ch==1:
    b=Bank()
    b.create_account()
    acclist.append(b)
  elif ch==2:
    searchno=int(input("Enter account number:"))
    flag=False
    for i in acclist:
      if i.accno==searchno:
        print(i)
        flag=True  
    if flag==False:
       print("Acount doesnt exist\ncreate  a account first")

  elif ch==3:
    searchno=int(input("Enter account number:"))
    flag=False
    for i in acclist:
      if i.accno==searchno:
        i.deposit_ammount()
        print(i)
        flag=True  
    if flag==False:
       print("Acount doesnt exist\ncreate  a account first")  
  elif ch==4:
    searchno=int(input("Enter account number:"))
    flag=False
    for i in acclist:
      if i.accno==searchno:
        i.withdraw_ammount()
        print(i)
        flag=True  
    if flag==False:
       print("Acount doesnt exist\ncreate  a account first")
    
  elif ch==0:
    print("Exiting.........")
    break  
  else:
    print("Error")
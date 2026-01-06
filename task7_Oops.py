#create a class name bank account 
#with best and required attributes and methods
#providing the services of deposit,withdraw, check balance
class Bankaccount:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
        self.transaction={}
        self.count=1
        self.history={}

    def deposit(self,amount):
        self.balance +=amount
        self.transaction[self.count]={'Type':'Deposit','Deposit_amount':amount,'Total_balance':self.balance}
        self.count+=1
        # self.history=history.append({'type':"deposit",'deposit':amount}) // mistake 
        
        return self.balance,self.history
        
        
    # def fund_transfer(self,targeted_account,amount):
    #     if self.balance>=amount:
    #         self.balance -= amount
    #         targeted_account.balance+=amount
    #         return {self.balance}
    #     else:
    #         return print("insuffient balance")
        

        

    # def withdraw(self,amount):
    #     if amount<=self.balance: 
    #         self.balance -=amount
    #         return self.balance
    #     else:
    #         return print("insufficent Balance")
        
    # def check_balance(self):
    #     return self.balance
    

    
account1=Bankaccount("bishwas",1234567890,10000)
account2=Bankaccount("manita",1234567891,20000)

print(account1.name)
print(account1.deposit(6000))
print(account1.withdraw(9000))
print(account1.check_balance())

print(account1.transaction)
account1.fund_transfer(account2,500)
account1.fund_transfer(account2,50000)
print(account2.balance)



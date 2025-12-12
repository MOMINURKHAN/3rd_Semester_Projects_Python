class BankAccount:
    def __init__(self,owner,balance,acc_num = 'A1312432'):
        self.owner = owner
        self.balance = balance
        self.acc_num = acc_num
        self.transection = []
    def input_validation(self,amount):
        if amount<=0:
            raise ValueError("Amount must be positive")
        return True

    def deposit(self,amount):
        if self.input_validation(amount):
            self.balance += amount
            self.transection.append(('deposit',amount))
            print(f'Account holder :  {self.owner}Deposited : {amount}. New Balance {self.balance}')
        return False
    def Withdraw(self,amount):
        if self.input_validation(amount):
            if amount>self.balance:
                print(f"withdraw request of {amount} is more than actual account balance {self.balance}")

            self.balance-=amount
            self.transection.append(('withdraw',amount))
            print(f"{self.owner} Withdrawl {amount}. New Balance {self.balance}")
            return True
        return False
    def show(self):
        print(f"{self.acc_num} : {self.owner} : {self.balance}")
    def transfer(self,amount,reciever_account):
        if self.Withdraw(amount):
            reciever_account.deposit(amount)
            reciever_account.transection.append(('transfer=in',amount,self.acc_num))
            print(f"transferred : {amount} to {reciever_account.owner}")
            return True 
        return False
    def show_transection(self):
        print(f"Transection history for {self.owner}")
        for transection in self.transection:
            print(f"    -{transection}"
                  )
        

    
Account_A = BankAccount('Prattoy_vai',5000,'A2352BY988')
Account_B = BankAccount('Hashitha',3500,'H24523243')
Account_A.deposit(3000)
Account_A.Withdraw(1300)
Account_A.show()
Account_A.transfer(int(input("Enter the amount you want to transfer :")),Account_B)
Account_A.show()
Account_B.show()
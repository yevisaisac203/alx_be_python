class BankAccount:
    def __init__(self,initial_balance = 0 ):
        self.account_balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount 
        else:
            return "deposit amount should be posoitive"
    def withdraw(self, amount):
         if amount > 0:
            if amount<= self.account_balance:
             self.account_balance -= amount
            return True
        
                      
         else:
            return False
    def display_balance(self):
        print(f"Current Balance:&{self.account_balance:}")
            
        
            
            
            
        
            
        
        
    
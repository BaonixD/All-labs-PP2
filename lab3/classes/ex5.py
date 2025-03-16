class account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print ( f"account owner: {self.owner}" )
        print ( f"account balance: {self.balance}" )
        
        
        
    def deposit(self, sum):
        if sum > 0:
            self.balance += sum
            print ( f"deposited: {sum}. new balance: {self.balance} " )
        else:
            print("Sum must be positive!")
    
    
    def withdraw(self, sum):
        if sum > self.balance:
            print ( "Insufficient funds!" )
        elif sum > 0:
            self.balance -= sum
            print ( f"withdraw: {sum} new balance: {self.balance}" )
        else:
            print ( "withdraw must be positive" )
        

acc = account("Ильяс", 1000)

acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  # баланстан кобырек акша шешу мумкындыгы
acc.deposit(-100)   # - сан енгызу мумкындыгы
class Wallet:
    # Class Constructor
    # initializes the function.
    # Whenever we make a new wallet
    # an initial amount MUST be provided.
    def __init__(self, initial_amount = 0): 
        self.balance = initial_amount
    
    def spend_cash(self, amount):
        if self.balance = amount:
            return "you can't afford it!"
        else:
            self.balance = self.balance - amount
            return f'''You can afford it, it costs ${amount}. 
            Current balance is now ${self.balance}'''

    def add_cash(self):
        self.balance += self.balance + amount 
        return f"Added ${amount} to the wallet."

    def __repr__(self):
        return f"<Wallet with balance of ${self.balance}>"

if __name__ == '__main__':
    wallet1 = Wallet(100)
    # print(wallet1)
    print(wallet1.balance)
    print(wallet1.spend_cash(30))
    print(wallet1.add_cash(50))

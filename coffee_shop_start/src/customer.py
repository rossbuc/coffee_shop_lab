class Customer:

    def __init__(self, name, wallet):
        self.name =  name
        self.wallet = wallet

    def change_wallet_amount(self, amount):
        self.wallet -= amount

    def buys_drink(self, drink):
        self.change_wallet_amount(drink.price)
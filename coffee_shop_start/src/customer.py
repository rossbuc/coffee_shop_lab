
class Customer:

    def __init__(self, name, wallet, age):
        self.name =  name
        self.wallet = wallet
        self.age = age
        self.energy = 0

    def change_wallet_amount(self, amount):
        self.wallet -= amount

    def buys_drink(self, drink):
        self.change_wallet_amount(drink.price)
        self.energy += drink.caffine

    def buys_food(self, food):
        self.change_wallet_amount(food.price)
        self.energy -= food.digestion_level
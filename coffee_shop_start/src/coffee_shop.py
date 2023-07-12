from src.drink import Drink

class CoffeeShop:
	
	

	def __init__(self, name, till):
		self.name = name
		self.till = till
		self.drinks = [Drink("espresso", 2, 7), Drink("americano", 1, 5), Drink("latte", 3, 3), Drink("mocho", 3, 4), Drink("cappuccino", 4, 6)]

	def change_till_by_amount(self, amount):
		self.till += amount

	def sell_drink(self, drink, customer):
		if customer.age >= 16 and customer.energy < 70:
			self.change_till_by_amount(drink.price)
		else:
			return "Sorry buddy, I can't serve you!"
	
	def drinks_customer_can_afford(self, customer):
		return [drink.name for drink in self.drinks if customer.wallet >= drink.price]

	def drink_names(self):
        	return [drink.name for drink in self.drinks]
	
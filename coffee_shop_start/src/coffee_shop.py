from src.drink import Drink

class CoffeeShop:
	
	def __init__(self, name, till):
		self.name = name
		self.till = till

		self.stock = {
			Drink("espresso", 2, 7): 100,
			Drink("americano", 1, 5): 150,
			Drink("latte", 3, 3): 80,
			Drink("mocho", 3, 4): 60,
			Drink("cappuccino", 4, 6): 120
		}

		self.value_of_stock = 0

	def change_till_by_amount(self, amount):
		self.till += amount

	def sell_drink(self, drink, customer):
		if customer.age >= 16 and customer.energy < 70:
			self.change_till_by_amount(drink.price)
		else:
			return "Sorry buddy, I can't serve you!"
	
	def drinks_customer_can_afford(self, customer):
		return [drink.name for drink in self.stock if customer.wallet >= drink.price]

	def sell_food(self, food):
		self.change_till_by_amount(food.price)

	def drink_names(self):
			return [drink.name for drink in self.stock]	

	def stock_value(self):
		for item in self.stock:
			self.value_of_stock += self.stock[item] * item.price	
		return self.value_of_stock

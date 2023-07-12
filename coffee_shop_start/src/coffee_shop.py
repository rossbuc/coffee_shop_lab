class CoffeeShop:
	
	def __init__(self, name, till):
		self.name = name
		self.till = till

	def change_till_by_amount(self, amount):
		self.till += amount

	def sell_drink(self, drink, customer):
		if customer.age >= 16 and customer.energy < 70:
			self.change_till_by_amount(drink.price)
		else:
			return "Sorry buddy, I can't serve you!"

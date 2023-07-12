class CoffeeShop:
	
	def __init__(self, name, till):
		self.name = name
		self.till = till

	def change_till_by_amount(self, amount):
		self.till += amount
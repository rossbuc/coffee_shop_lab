import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink
from src.customer import Customer

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100)
        self.drink = Drink("espresso", 2)
        self.customer = Customer("Buddy", 10, 15)
        self.customer_2 = Customer("Sweep", 50, 60)
    
    def test_coffee_shop_has_name(self):
        self.assertEqual("The Prancing Pony", self.coffee_shop.name)

    def test_coffee_shop_has_till(self):
        self.assertEqual(100, self.coffee_shop.till)

    def test_increase_till(self):
        self.coffee_shop.change_till_by_amount(10)
        self.assertEqual(110, self.coffee_shop.till)

    def test_decrease_till(self):
        self.coffee_shop.change_till_by_amount(-10)
        self.assertEqual(90, self.coffee_shop.till)

    @unittest.skip("Old test for testing the shop can sell a drink")
    def test_can_sell_drink(self):
        self.coffee_shop.sell_drink(self.drink)
        self.assertEqual(102, self.coffee_shop.till)

    def test_no_sale_under_16(self):
        result = self.coffee_shop.sell_drink(self.drink, self.customer)
        self.assertEqual("Too young, Buddy!", result)

    def test_sale_if_over_16(self):
        self.coffee_shop.sell_drink(self.drink, self.customer_2)
        self.assertEqual(102, self.coffee_shop.till)
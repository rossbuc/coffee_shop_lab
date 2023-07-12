import unittest
from src.coffee_shop import CoffeeShop
from src.drink import Drink

class TestCoffeeShop(unittest.TestCase):

    def setUp(self):
        self.coffee_shop = CoffeeShop("The Prancing Pony", 100)
        self.drink = Drink("espresso", 2)
    
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

    def test_can_sell_drink(self):
        self.coffee_shop.change_till_by_amount(self.drink.price)
        self.assertEqual(102, self.coffee_shop.till)
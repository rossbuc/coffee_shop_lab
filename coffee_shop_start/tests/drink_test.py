import unittest
from src.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("espresso", 2)

    def test_drink_has_name(self):
        self.assertEqual("espresso", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(2, self.drink.price)
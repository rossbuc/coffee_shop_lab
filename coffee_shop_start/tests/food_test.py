import unittest
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.food = Food("cookie", 3, 6)

    def test_food_has_name(self):
        self.assertEqual("cookie", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(3, self.food.price)

    def test_food_has_digestion_level(self):
        self.assertEqual(6, self.food.digestion_level)
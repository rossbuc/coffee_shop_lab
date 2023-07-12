import unittest
from src.customer import Customer
from src.drink import Drink

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Buddy", 10)
        self.drink = Drink("espresso", 2)

    def test_customer_has_name(self):
        self.assertEqual("Buddy", self.customer.name)

    def test_customer_has_money(self):
        self.assertEqual(10, self.customer.wallet)

    def test_change_amount_wallet(self):
        self.customer.change_wallet_amount(5)
        self.assertEqual(5, self.customer.wallet)

    @unittest.skip("This was to test input to buys_drink method was object")
    def test_customer_gets_drink(self):
        self.assertIsInstance(self.customer.buys_drink, object)
    
    def test_customer_can_buy_drink(self):
        self.customer.buys_drink(self.drink)
        self.assertEqual(8, self.customer.wallet)
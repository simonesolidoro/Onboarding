import unittest
from carrello import Cart, Product,CartItem

class TestCart(unittest.TestCase):
    def test_total_price(self):
        cart = Cart()
        for i in range(10):
            cart.add_product(Product("quaderno",5))
            cart.add_product(Product("matita",1))
        cart.remove_product(Product("quaderno",5))
        self.assertEqual(55, cart.total_price())  # add assertion here


if __name__ == '__main__':
    unittest.main()

import pytest
from carrello import Cart, Product,CartItem

@pytest.mark.parametrize("number_item,expected",
                         [(1,1),
                          (2,7),
                          (3,13)])
def test_tot_price(number_item,expected):
    cart = Cart()
    price_quaderno = 5.0
    price_matita = 1.0
    for i in range(number_item):
        cart.add_product(Product("quaderno",price_quaderno))
        cart.add_product(Product("matita",price_matita))
    cart.remove_product(Product("quaderno",price_quaderno))
    #expected = number_item*price_matita+ (number_item-1)*price_quaderno
    assert expected == cart.total_price()  # add assertion here


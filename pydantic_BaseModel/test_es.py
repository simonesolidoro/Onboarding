import pytest
from pydantic import ValidationError

from main import User,Product,LineItem,Order

def test_user():
    u1 = User(id=1, name='psp', email='simosoli00@gmail.com', age=19, is_active=True)
    u2 = User(id = "2", name = "simo", email = "s@k.it")

def test_user_invalid():
    with pytest.raises(ValidationError):
        u1 = User(id=1, name='psp', email='simoso@li00@gmail.com', age=19, is_active=True)
    with pytest.raises(ValidationError):
        u2 = User(id="str", name='psp', email='simosoli00@gmail.com', age=19, is_active=True)

def test_validator_mail():
    with pytest.raises(ValueError):
        u =  User(id=1, name='psp', email='simoso@li00@tempmail.com', age=19, is_active=True)

def test_active_age():
    with pytest.raises(ValueError):
        u =  User(id=1, name='psp', email='simoso@li00@gmail.com', age=17, is_active=True)

def test_ecommerce():
    quaderno = Product(id = 1, name = "quaderno", cost = 2)
    matita = Product(id = 2, name = "matita", cost = 1)

    matite = LineItem(product=matita,quantity=3)
    quaderni = LineItem(product=quaderno,quantity=2)

    ordine = Order(items=[matite, quaderni])
    assert ordine.total_cost == 7

def test_parse():
    json_data = {"items": [{"product": {"id": 2, "name": "matita", "cost": 1.0}, "quantity": 3, "total_cost": 3.0},
               {"product": {"id": 1, "name": "quaderno", "cost": 2.0}, "quantity": 2, "total_cost": 4.0}],
     "total_cost": 7.0}
    order = Order.model_validate(json_data)
    assert order.total_cost == 7

class Product:
    def __init__(self, name, price: float):
        self.name = name
        self.price = price
    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
    def __str__(self):
        return self.name
class  CartItem:
    def __init__(self,prod,quantity):
        self.product = prod
        self.quantity = quantity
    def price(self):
        return self.product.price* self.quantity

class Cart:
    def __init__(self):
        self.items = []
    def add_product(self, prod : Product):
        find = False
        for item in self.items:
            if item.product == prod:
                find = True
                item.quantity += 1
        if find == False:
            self.items.append(CartItem(prod,1))
    def remove_product(self, prod : Product):
        for item in self.items:
            if item.product == prod:
                if item.quantity == 1:
                    self.items.remove(item)
                else:
                    item.quantity -= 1
            break

    def total_price(self):
        tot = 0.0
        for item in self.items:
            tot += item.price()
        return tot
from pydantic import BaseModel, Field, field_validator, EmailStr, computed_field, model_validator

class User(BaseModel):
    id: int
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    age: int = Field(default=18, gt=0, lt = 120)
    is_active: bool = True

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        if value.endswith("@tempmail.com"):
            raise ValueError("dominio tempmail.com non va bene")
        return value

    @model_validator(mode="after")
    def validate_active_age(self):
        if self.is_active and self.age < 18:
            raise ValueError("Un active deve avere almeno 18 anni")
        return self


class Product(BaseModel):
    id : int
    name : str
    cost : float = Field(gt = 0)
class LineItem(BaseModel):
    product: Product
    quantity: int = Field(default = 0, gt=0)
    @computed_field
    def total_cost(self)->float:
        return self.product.cost * self.quantity
    # def __add__(self,other):
    #     if not isinstance(other,LineItem):
    #         raise ValueError ("somma solo con altro lineItem")
    #     return self.total_cost()+other.total_cost()

class Order(BaseModel):
    items : list[LineItem]
    @computed_field
    @property
    def total_cost(self) -> float:
        tot = 0.0
        for item in self.items:
            tot += item.total_cost
        return tot

quaderno = Product(id = 1, name = "quaderno", cost = 2)
matita = Product(id = 2, name = "matita", cost = 1)

matite = LineItem(product=matita,quantity=3)
quaderni = LineItem(product=quaderno,quantity=2)

ordine = Order(items=[matite, quaderni])
print(ordine.model_dump_json())
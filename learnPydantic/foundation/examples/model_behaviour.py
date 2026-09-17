from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_legth(cls, value):
        if value < 4:
            raise ValueError("User name lenght must be more that 4 character")
        return value

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password don not match')
        return values

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

product = Product(price=100, quantity=3)

print(product.price)
# 100

print(product.quantity)
# 3

print(product.total_price) # we don't call a method here because fo property decorator it acts like a value
# 300
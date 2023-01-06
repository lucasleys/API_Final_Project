from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    category: str


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    location_id: int
    customer_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    products: list[Product] = []

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    city: str
    zipcode: int
    chief: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int
    products: list[Product] = []

    class Config:
        orm_mode = True
from pydantic import BaseModel


class PurchaseBase(BaseModel):
    pass


class PurchaseCreate(PurchaseBase):
    pass


class Purchase(PurchaseBase):
    id: int
    customer_id: int
    product_id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    price: float
    category: str
    barcode: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    location_id: int
    customer_id: int

    products: list[Purchase] = []

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: str = None
    price: float = None
    category: str = None
    location_id: int = None
    customer_id: int = None


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    purchases: list[Purchase] = []

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    city: str | None = None
    zipcode: int
    chief: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int

    branch: list[Product] = []

    class Config:
        orm_mode = True



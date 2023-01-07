from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    customers = relationship("Purchase", back_populates="purchases")


class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    purchases = relationship("User", back_populates="customers")
    bought_products = relationship("Product", back_populates="products")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float, index=True)
    category = Column(String, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))

    products = relationship("Purchase", back_populates="bought_products")
    branch = relationship("Location", back_populates="stock")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    zipcode = Column(Integer, unique=True, index=True)
    chief = Column(String,unique=True, index=True)

    stock = relationship("Product", back_populates="branch")





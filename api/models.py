from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    customers = relationship("User", back_populates="")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float, index=True)
    category = Column(String, index=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    customer_id = Column(Integer, ForeignKey("users.id"))

    customer = relationship("User", back_populates="customers")
    branch = relationship("Location", back_populates="products")


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    zipcode = Column(Integer, unique=True, index=True)
    chief = Column(String, index=True)







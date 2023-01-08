from sqlalchemy.orm import Session
from sqlalchemy import func

import models
import schemas
import auth


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(name=user.name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_product(db: Session, product: schemas.ProductCreate):
    # if product is not None:
    #     db_product = models.Product(**product.dict(), customer_id=customer_id)
    #     db.add(db_product)
    #     db.commit()
    #     db.refresh(db_product)
    #     return db_product
    #
    # else:
    #     return product

    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, product_name: str):
    return db.query(models.Product).filter(models.Product.name == product_name).first()


def create_location(db: Session, location: schemas.LocationCreate):
    db_location = models.Location(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).offset(skip).limit(limit).all()


def get_location(db: Session, location_id: int):
    return db.query(models.Location).filter(models.Location.id == location_id).first()


def update_product(db: Session, product: schemas.Product, update: schemas.ProductUpdate):
    for key, value in update.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int):
    product = db.get(models.Product, product_id)
    if not product:
        return None
    db.delete(product)
    db.commit()
    return {"Product removed": True}

# def get_products_in_location(db: Session, city: str):
#     products_per_location = {
#         db.query(models.Location.city, func.count(models.Product.id))
#             .join(models.Product)
#             .filter(models.Location.city == city)
#             .group_by(models.Location.city)
#             .all()
#     }
#
#     return products_per_location
#
#
# def get_bought_products(db: Session, user_id: int):
#     bought_products_per_user = {
#         db.query(models.User.id)
#             .join(models.Product)
#             .filter(models.User.id == user_id)
#             .order_by(models.Product.id)
#             .all()
#     }
#
#     return bought_products_per_user
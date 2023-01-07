from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="name already listed")
    return crud.create_user(db=db, user=user)


@app.get("/products/", response_model=list[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@app.post("/product/{location_id}/location", response_model=schemas.Product)
def create_product(location_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product = crud.get_product(db, product.barcode)
    if product:
        raise HTTPException(status_code=400, detail="product already listed")
    return crud.create_product(db=db, product=product, location_id=location_id)


@app.put("/product/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, update: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    return crud.update_product(db=db, product=product, update=update)


@app.delete("/product/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.delete_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    return product


@app.get("/locations/", response_model=list[schemas.Location])
def get_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations


@app.post("/location/", response_model=schemas.Location)
def create_user(location: schemas.LocationCreate, db: Session = Depends(get_db)):
    location = crud.get_location(db, location.zipcode)
    if location:
        raise HTTPException(status_code=400, detail="location already listed")
    return crud.create_location(db=db, location=location)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/api/products")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.ProductOut])
def get_all(page: int = 1, db: Session = Depends(get_db)):
    skip = (page - 1) * 10
    return crud.get_products(db, skip)


@router.get("/{id}", response_model=schemas.ProductOut)
def get_one(id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, id)


@router.post("/", response_model=schemas.ProductOut)
def create(data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, data)


@router.put("/{id}", response_model=schemas.ProductOut)
def update(id: int, data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.update_product(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, id)
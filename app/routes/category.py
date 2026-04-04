from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter(prefix="/api/categories")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=List[schemas.CategoryOut])
def get_all(page: int = 1, db: Session = Depends(get_db)):
    skip = (page - 1) * 10
    return crud.get_categories(db, skip)


@router.get("/{id}", response_model=schemas.CategoryOut)
def get_one(id: int, db: Session = Depends(get_db)):
    return crud.get_category(db, id)


@router.post("/", response_model=schemas.CategoryOut)
def create(data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, data)


@router.put("/{id}", response_model=schemas.CategoryOut)
def update(id: int, data: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.update_category(db, id, data)


@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return crud.delete_category(db, id)
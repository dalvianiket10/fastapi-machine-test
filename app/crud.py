from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models


# CATEGORY
def get_categories(db: Session, skip=0, limit=10):
    return db.query(models.Category).offset(skip).limit(limit).all()


def get_category(db: Session, id: int):
    obj = db.query(models.Category).filter(models.Category.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")
    return obj


def create_category(db: Session, data):
    obj = models.Category(name=data.name)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_category(db: Session, id: int, data):
    obj = db.query(models.Category).filter(models.Category.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")

    obj.name = data.name
    db.commit()
    db.refresh(obj)
    return obj


def delete_category(db: Session, id: int):
    obj = db.query(models.Category).filter(models.Category.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(obj)
    db.commit()
    return {"message": "Category deleted successfully"}


# PRODUCT
def get_products(db: Session, skip=0, limit=10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def get_product(db: Session, id: int):
    obj = db.query(models.Product).filter(models.Product.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Product not found")
    return obj


def create_product(db: Session, data):
    # check category exists
    category = db.query(models.Category).filter(
        models.Category.id == data.category_id
    ).first()

    if not category:
        raise HTTPException(status_code=400, detail="Invalid category_id")

    obj = models.Product(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_product(db: Session, id: int, data):
    obj = db.query(models.Product).filter(models.Product.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Product not found")

    category = db.query(models.Category).filter(
        models.Category.id == data.category_id
    ).first()

    if not category:
        raise HTTPException(status_code=400, detail="Invalid category_id")

    obj.name = data.name
    obj.price = data.price
    obj.category_id = data.category_id

    db.commit()
    db.refresh(obj)
    return obj


def delete_product(db: Session, id: int):
    obj = db.query(models.Product).filter(models.Product.id == id).first()
    if not obj:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(obj)
    db.commit()
    return {"message": "Product deleted successfully"}
from pydantic import BaseModel

# CATEGORY
class CategoryCreate(BaseModel):
    name: str

class CategoryOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


# PRODUCT
class ProductCreate(BaseModel):
    name: str
    price: int
    category_id: int

class ProductOut(BaseModel):
    id: int
    name: str
    price: int
    category: CategoryOut   # important

    class Config:
        from_attributes = True
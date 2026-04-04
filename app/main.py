from fastapi import FastAPI
from .database import Base, engine
from .routes import category, product

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(category.router)
app.include_router(product.router)
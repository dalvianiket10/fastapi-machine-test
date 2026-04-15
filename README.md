# 🚀 FastAPI Machine Test

## 📌 Project Overview
This project is a backend application built using FastAPI that provides RESTful APIs for managing Categories and Products.  
It follows a clean architecture with SQLAlchemy ORM and PostgreSQL database integration.

---

## 🛠 Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy (ORM)
- Pydantic
- Uvicorn

---

## ✨ Features
- Category CRUD Operations
- Product CRUD Operations
- One-to-Many Relationship (Category → Products)
- Server-side Pagination
- Clean API structure using FastAPI routers

---

## 🗂 Project Structure
```
app/
│── main.py
│── database.py
│── models.py
│── schemas.py
│── crud.py
│
└── routes/
    ├── category.py
    └── product.py
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/dalvianiket10/fastapi-machine-test.git
cd fastapi-machine-test
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Server
```bash
uvicorn app.main:app --reload
```

---

## 📡 API Endpoints

### 📂 Categories
| Method | Endpoint | Description |
|--------|---------|------------|
| POST   | /api/categories/ | Create category |
| GET    | /api/categories/?page=1 | Get all categories (pagination) |
| GET    | /api/categories/{id} | Get category by ID |
| PUT    | /api/categories/{id} | Update category |
| DELETE | /api/categories/{id} | Delete category |

---

### 📦 Products
| Method | Endpoint | Description |
|--------|---------|------------|
| POST   | /api/products/ | Create product |
| GET    | /api/products/?page=1 | Get all products (pagination) |
| GET    | /api/products/{id} | Get product by ID |
| PUT    | /api/products/{id} | Update product |
| DELETE | /api/products/{id} | Delete product |

---

## 🔗 Database Design

### Category Table
- id (Primary Key)
- name

### Product Table
- id (Primary Key)
- name
- price
- category_id (Foreign Key)

👉 Relationship:
- One Category → Many Products

---

## 📄 Sample API Response
```json
{
  "id": 1,
  "name": "Mobile",
  "price": 20000,
  "category": {
    "id": 1,
    "name": "Electronics"
  }
}
```

---

## 📌 Notes
- Pagination implemented using query parameter `page`
- Each product includes associated category details

---

## 👨‍💻 Author
**Aniket Dalvi**
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models import Product, Package, Nutritionist, Order, Payment, HealthData
from app.schemas import ProductCreate, PackageCreate, OrderCreate, PaymentCreate
from app.services import create_product, create_package, create_order, create_payment
from app.auth import get_current_user, User

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS settings
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://example.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Route to create a new product
@app.post("/products/", response_model=ProductCreate)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to create products")
    return create_product(db=db, product=product)

# Route to create a new package
@app.post("/packages/", response_model=PackageCreate)
def create_new_package(package: PackageCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized to create packages")
    return create_package(db=db, package=package)

# Route to create a new order
@app.post("/orders/", response_model=OrderCreate)
def create_new_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_order(db=db, order=order, user_id=current_user.id)

# Route to create a new payment
@app.post("/payments/", response_model=PaymentCreate)
def create_new_payment(payment: PaymentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_payment(db=db, payment=payment, user_id=current_user.id)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}
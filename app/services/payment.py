from sqlalchemy.orm import Session
from app.models import Payment, Order
from app.schemas import PaymentCreate
from fastapi import HTTPException, status

# Service function to create a new payment
def create_payment(db: Session, payment: PaymentCreate, user_id: int) -> Payment:
    # Check if the order exists and belongs to the user
    order = db.query(Order).filter(Order.id == payment.order_id, Order.user_id == user_id).first()
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found or not authorized")

    # Create a new payment record
    db_payment = Payment(
        order_id=payment.order_id,
        user_id=user_id,
        amount=payment.amount,
        status=payment.status,
        payment_method=payment.payment_method
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

# Service function to process a payment
def process_payment(payment_id: int, db: Session) -> Payment:
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

    # Simulate payment processing logic
    if payment.status == "Pending":
        payment.status = "Completed"  # Assume payment is successful
        db.commit()
        db.refresh(payment)
    return payment

# Service function to refund a payment
def refund_payment(payment_id: int, db: Session) -> Payment:
    payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if not payment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payment not found")

    # Simulate refund logic
    if payment.status == "Completed":
        payment.status = "Refunded"
        db.commit()
        db.refresh(payment)
    return payment
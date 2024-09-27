from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Subscription
from schema import SubscriptionCreate, SubscriptionRead
import datetime

router = APIRouter()

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/subscriptions/", response_model=SubscriptionRead)
def create_subscription(subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = Subscription(
        user_id=subscription.user_id,
        topic=subscription.topic,
        email=subscription.email,
        phone=subscription.phone,
        subscription_date=str(datetime.datetime.now()),  # Usar la fecha actual
        active=subscription.active,
        notification_type=subscription.notification_type,
        additional_info=subscription.additional_info
    )
    db.add(db_subscription)
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@router.get("/subscriptions/", response_model=list[SubscriptionRead])
def read_all_subscriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subscriptions = db.query(Subscription).offset(skip).limit(limit).all()
    return subscriptions

@router.get("/subscriptions/{subscription_id}", response_model=SubscriptionRead)
def read_subscription(subscription_id: int, db: Session = Depends(get_db)):
    subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")
    return subscription

@router.put("/subscriptions/{subscription_id}", response_model=SubscriptionRead)
def update_subscription(subscription_id: int, subscription: SubscriptionCreate, db: Session = Depends(get_db)):
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")

    # Actualiza los campos
    db_subscription.user_id = subscription.user_id
    db_subscription.topic = subscription.topic
    db_subscription.email = subscription.email
    db_subscription.phone = subscription.phone
    db_subscription.active = subscription.active
    db_subscription.notification_type = subscription.notification_type
    db_subscription.additional_info = subscription.additional_info
    db.commit()
    db.refresh(db_subscription)
    return db_subscription

@router.delete("/subscriptions/{subscription_id}", response_model=dict)
def delete_subscription(subscription_id: int, db: Session = Depends(get_db)):
    db_subscription = db.query(Subscription).filter(Subscription.id == subscription_id).first()
    if db_subscription is None:
        raise HTTPException(status_code=404, detail="Subscription not found")

    db.delete(db_subscription)
    db.commit()
    return {"detail": "Subscription deleted"}

from pydantic import BaseModel
from datetime import datetime

class SubscriptionCreate(BaseModel):
    user_id: int
    topic: str
    email: str
    phone: str
    active: str
    notification_type: str
    additional_info: str

class SubscriptionRead(BaseModel):
    id: int
    user_id: int
    topic: str
    email: str
    phone: str
    subscription_date: datetime
    active: str
    notification_type: str
    additional_info: str

    class Config:
        orm_mode = True  # Permite que se convierta de ORM a Pydantic

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from observer import notify_observers

router = APIRouter()

class Message(BaseModel):
    message: str

@router.post("/publish/{topic}")
async def publish(topic: str, message: Message):
    try:
        await notify_observers(topic, message.message)  
        return {"message": f"Message sent to {topic}"}
    except KeyError:
        raise HTTPException(status_code=404, detail="Topic not found")

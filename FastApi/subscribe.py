from fastapi import APIRouter, WebSocket, Depends
from sqlalchemy.orm import Session
from observer import add_observer
from database import SessionLocal, Subscription
import datetime
import json

router = APIRouter()

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.websocket("/subscribe/{topic}")
async def websocket_subscribe(websocket: WebSocket, topic: str, db: Session = Depends(get_db)):
    await websocket.accept()
    print(f"Conexión aceptada para el tema: {topic}")

    try:
        # Recibir datos del usuario
        user_data = await websocket.receive_text()
        user_data = json.loads(user_data)

        user_id = user_data.get("user_id")
        email = user_data.get("email")
        phone = user_data.get("phone")
        notification_type = user_data.get("notification_type")
        additional_info = user_data.get("additional_info")

        # Agregar el observador
        add_observer(topic, websocket)

        # Guardar la suscripción en la base de datos
        subscription = Subscription(
            user_id=user_id,
            topic=topic,
            email=email,
            phone=phone,
            subscription_date=str(datetime.datetime.now()),
            active='active',
            notification_type=notification_type,
            additional_info=additional_info
        )
        db.add(subscription)
        db.commit()
        db.refresh(subscription)
        
        print("Suscripción guardada:", subscription)

        while True:
            data = await websocket.receive_text()
            print(f"Mensaje recibido: {data}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await websocket.close()
        print("Conexión cerrada")

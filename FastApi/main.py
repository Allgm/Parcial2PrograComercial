from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from subscribe import router as subscribe_router
from publish import router as publish_router
from crud import router as subscription_router  # Cambié de subscribe a crud

app = FastAPI()

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluyendo los routers
app.include_router(subscribe_router)
app.include_router(publish_router)
app.include_router(subscription_router)

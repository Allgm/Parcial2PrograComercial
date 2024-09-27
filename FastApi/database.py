from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root@localhost/parcial2"  

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, Sequence('subscription_id_seq'), primary_key=True)
    user_id = Column(Integer, index=True)  
    topic = Column(String, index=True) 
    email = Column(String, index=True) 
    phone = Column(Integer, index=True) 
    subscription_date = Column(String) 
    active = Column(String)  
    notification_type = Column(String)  
    additional_info = Column(String)  

Base.metadata.create_all(bind=engine)

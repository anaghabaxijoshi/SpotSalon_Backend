from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from typing import Optional

class Base(DeclarativeBase):
    pass

class BaseModel:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Base(DeclarativeBase):
    pass


class Profile(Base, BaseModel):
    __tablename__ = 'profile'
    spot_id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    role:Mapped[str] = mapped_column(String(100), nullable=False)
    name:Mapped[str] = mapped_column(String(200), nullable=False)
    email_id:Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password:Mapped[str] = mapped_column(String(100),nullable=False)
   
    
class SalonContact(Base, BaseModel):
    __tablename__ = 'salon_contact'
    contact_id:Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key= True)
    spot_id:Mapped[int] = mapped_column(Integer, ForeignKey("profile.spot_id", onupdate="CASCADE", ondelete="CASCADE"))
    phone:Mapped[int] = mapped_column(Integer, nullable=False)
    city:Mapped[str] = mapped_column(String(100), nullable=False)
    state:Mapped[Optional[str]] = mapped_column(String(100))
    country:Mapped[str] = mapped_column(String(100), nullable=False)
    address:Mapped[str] = mapped_column(String(200), nullable=False)
    opening_time:Mapped[datetime] = mapped_column(DateTime)
    closing_time:Mapped[datetime] = mapped_column(DateTime)

class SalonServices(Base, BaseModel):
    __tablename__ = 'salon_services'
    service_id:Mapped[int] = mapped_column(Integer, autoincrement= True, primary_key= True)
    spot_id:Mapped[int] = mapped_column(Integer, ForeignKey("profile.spot_id", onupdate="CASCADE", ondelete="CASCADE"))
    hair:Mapped[Optional[str]] = mapped_column(String(50))
    skin:Mapped[Optional[str]] = mapped_column(String(50))
    nails:Mapped[Optional[str]] = mapped_column(String(50))
    massage:Mapped[Optional[str]] = mapped_column(String(50))
    wax:Mapped[Optional[str]] = mapped_column(String(50))
    makeup:Mapped[Optional[str]] = mapped_column(String(50))
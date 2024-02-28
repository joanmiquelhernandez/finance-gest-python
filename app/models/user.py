import uuid

from datetime import datetime

from typing import List
from sqlalchemy import ForeignKey, Integer, MetaData, String, DateTime, Boolean, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.account import BankAccount
from app.models.movement import Movement
class User(Base):
    __tablename__ = 'user'

    id                  : Mapped[int]   = mapped_column(Integer, primary_key=True)
    username            : Mapped[str]   = mapped_column(String(80), unique=True)
    password            : Mapped[str]   = mapped_column(String(80))
    email               : Mapped[str]   = mapped_column(String(80), unique=True)
    create_datetime     : Mapped[str]   = mapped_column(DateTime(), nullable=False, server_default=func.now())
    update_datetime     : Mapped[str]   = mapped_column(DateTime(), nullable=False, server_default=func.now(), onupdate=datetime.utcnow)
    profile_picture     : Mapped[str]   = mapped_column(Text(), nullable=True)
    alt_id              : Mapped[str]   = mapped_column(String(80), unique=True, default=uuid.uuid4().hex)
    is_active           : Mapped[bool]  = mapped_column(Boolean, default=True)

    movements           : Mapped[Movement]  = relationship(back_populates='user')
    accounts            : Mapped[List[BankAccount]] = relationship(secondary='user_account', back_populates='users')

import uuid

from datetime import datetime

from typing import List
from sqlalchemy import ForeignKey, Integer, MetaData, String, DateTime, Boolean, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.movement import Movement

class MovementCategory(Base):
    __tablename__ = 'movement_category'

    id                  : Mapped[int]   = mapped_column(Integer, primary_key=True)
    name                : Mapped[str]   = mapped_column(String)
    is_income           : Mapped[bool]  = mapped_column(Boolean)
    is_active           : Mapped[bool]  = mapped_column(Boolean, default=True)
    bank_account_id     : Mapped[int]   = mapped_column(ForeignKey('bank_account.id'))

    bank_account        : Mapped['BankAccount']   = relationship(back_populates='movement_categories')
    movements           : Mapped[Movement]      = relationship(back_populates='category')

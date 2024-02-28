import uuid

from datetime import datetime

from typing import List
from sqlalchemy import ForeignKey, Integer, MetaData, String, DateTime, Boolean, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base

class Movement(Base):
    __tablename__ = 'movement'

    id                      : Mapped[int]       = mapped_column(Integer, primary_key=True)
    name                    : Mapped[str]       = mapped_column(String)
    amount                  : Mapped[int]       = mapped_column(Integer, default=0)
    creation_datetime       : Mapped[datetime]  = mapped_column(DateTime, default=func.now)
    last_modify_datetime    : Mapped[datetime]  = mapped_column(DateTime, nullable=True)
    category_id             : Mapped[int]       = mapped_column(ForeignKey('movement_category.id'))
    bank_account            : Mapped[int]       = mapped_column(ForeignKey('bank_account.id'))
    user_id                 : Mapped[int]       = mapped_column(ForeignKey('user.id'))

    user                    : Mapped['User']              = relationship(back_populates='movements')
    category                : Mapped['MovementCategory']  = relationship(back_populates='movements')
    account                 : Mapped['BankAccount']       = relationship(back_populates='movements')
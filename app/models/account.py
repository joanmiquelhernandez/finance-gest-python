from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, Integer, MetaData, String, DateTime, Boolean, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models import Base
from app.models.category import MovementCategory
from app.models.movement import Movement

class BankAccount(Base):
    __tablename__ = 'bank_account'

    id                  : Mapped[int]       = mapped_column(Integer, primary_key=True)
    name                : Mapped[str]       = mapped_column(String)
    color               : Mapped[str]       = mapped_column(String, default='#000000')
    picture             : Mapped[str]       = mapped_column(String, nullable=True)
    creation_date       : Mapped[datetime]  = mapped_column(DateTime, default=func.now)
    expiration_date     : Mapped[datetime]  = mapped_column(DateTime, nullable=True)
    is_active           : Mapped[bool]      = mapped_column(Boolean, default=True)

    movement_categories : Mapped[MovementCategory]  = relationship(back_populates='bank_account')
    movements           : Mapped[Movement]          = relationship(back_populates='account')
    users               : Mapped[List['User']]        = relationship(secondary='user_account', back_populates='accounts')

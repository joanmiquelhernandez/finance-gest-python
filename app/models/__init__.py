from flask import current_app
from sqlalchemy import Integer, MetaData, String, DateTime, Boolean, create_engine, func
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column

from app.config import config

engine = create_engine(config['development'].SQLALCHEMY_DATABASE_URI, pool_size=20) #, echo=True)

metadata = MetaData()


class Base(DeclarativeBase):
    metadata = metadata


    def as_dict(self):
        return {
           c.name: getattr(self, c.name) for c in self.__table__.columns
        }


def init_db():
    Base.metadata.create_all(engine)

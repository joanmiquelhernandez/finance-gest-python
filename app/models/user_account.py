from app.models import Base
from sqlalchemy import Column, Table, ForeignKey, String

user_account = Table(
    'user_account',
    Base.metadata,
    Column('user_is', ForeignKey('user.id')),
    Column('account_id', ForeignKey('bank_account.id')),
)

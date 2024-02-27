from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import engine

Session = scoped_session(sessionmaker(bind=engine))

session = Session()

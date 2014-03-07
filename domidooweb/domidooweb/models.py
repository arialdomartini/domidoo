from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension
import uuid


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class Place(Base):
    __tablename__ = 'places'
    id = Column(Text, primary_key=True)
    name = Column(Text)
    city = Column(Text)
    image = Column(Text)

    def __init__(self, name, city, image):
        self.id = str(uuid.uuid4())
        self.name = name
        self.city = city
        self.image = image

Index('place_name', Place.name, unique=True)

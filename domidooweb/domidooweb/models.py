from sqlalchemy import Column
from sqlalchemy import Index
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension
import uuid


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


places_tags = Table('places_tags', Base.metadata,
    Column('place_id', Integer, ForeignKey('places.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class Place(Base):
    __tablename__ = 'places'
    id = Column(Text, primary_key=True)
    name = Column(Text)
    city = Column(Text)
    image = Column(Text)

    tags = relationship('Tag', secondary=places_tags, backref='places')

    def __init__(self, name, city, image):
        self.id = str(uuid.uuid4())
        self.name = name
        self.city = city
        self.image = image


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Text, primary_key=True)
    name = Column(Text)

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name


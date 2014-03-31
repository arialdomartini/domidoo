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
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

import uuid


DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


places_tags = Table('places_tags', Base.metadata,
    Column('place_id', Integer, ForeignKey('places.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

from collections import OrderedDict
class DictSerializable(object):
    def to_json(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result

class Place(Base, DictSerializable):
    __tablename__ = 'places'
    id = Column(Text, primary_key=True)
    name = Column(Text)
    city = Column(Text)

    tags = relationship('Tag', secondary=places_tags, backref='places')


    def __init__(self, name, city, id = None):
        self.id = str(uuid.uuid4()) if id == None else id
        self.name = name
        self.city = city


class Image(Base, DictSerializable):
    __tablename__ = 'images'
    id = Column(Text, primary_key=True)
    filename = Column(Text)
    place_id = Column(Text, ForeignKey('places.id'))
    place = relationship("Place", backref=backref('images', order_by=id))

    def __init__(self, filename, place):
        self.id = str(uuid.uuid4())
        self.filename = filename
        self.place = place


class Tag(Base, DictSerializable):
    __tablename__ = 'tags'
    id = Column(Text, primary_key=True)
    name = Column(Text)

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name


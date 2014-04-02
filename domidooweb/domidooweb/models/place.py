import uuid

from sqlalchemy import Text
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Table
from sqlalchemy import ForeignKey

from domidooweb.dict_serializable import DictSerializable
from domidooweb.models.base import Base


places_tags = Table('places_tags', Base.metadata,
    Column('place_id', Integer, ForeignKey('places.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

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



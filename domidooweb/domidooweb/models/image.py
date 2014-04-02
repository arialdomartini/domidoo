import uuid

from sqlalchemy import Column, Text, ForeignKey
from sqlalchemy.orm import relationship, backref

from domidooweb.dict_serializable import DictSerializable
from domidooweb.models.base import Base


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
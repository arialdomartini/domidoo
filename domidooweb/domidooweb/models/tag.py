import uuid

from sqlalchemy import Column, Text

from domidooweb import Base
from domidooweb.dict_serializable import DictSerializable


class Tag(Base, DictSerializable):
    __tablename__ = 'tags'
    id = Column(Text, primary_key=True)
    name = Column(Text)

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name

from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import DBSession
from .models import Place
from .models import Tag
from sqlalchemy.orm.exc import NoResultFound

class PlaceRepository(object):
    def get_first(self):
        return DBSession.query(Place).first()

    def get(self, id):
        return DBSession.query(Place).filter(Place.id == id).one()

    def get_all(self):
        return DBSession.query(Place).all()

class TagRepository(object):

    def get_or_create_by_name(self, name):
        try:
            return DBSession.query(Tag).filter(Tag.name == name).one()
        except NoResultFound:
            return Tag(name)

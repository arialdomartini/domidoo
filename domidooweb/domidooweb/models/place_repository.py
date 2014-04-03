from domidooweb import DBSession
from domidooweb.models.place import Place

__author__ = 'arialdomartini'


class PlaceRepository(object):
    def get_first(self):
        return DBSession.query(Place).first()

    def get(self, id):
        return DBSession.query(Place).filter(Place.id == id).one()

    def get_all(self):
        return DBSession.query(Place).all()
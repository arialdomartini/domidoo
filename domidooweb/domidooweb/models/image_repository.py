from domidooweb import DBSession
from domidooweb.models.image import Image

__author__ = 'arialdomartini'


class ImageRepository(object):
    def get(self, id):
        return DBSession.query(Image).filter(Image.id == id).one()
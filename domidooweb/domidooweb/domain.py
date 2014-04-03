from domidooweb.models.base import DBSession
from domidooweb.models.image import Image


class ImageRepository(object):
    def get(self, id):
        return DBSession.query(Image).filter(Image.id == id).one()

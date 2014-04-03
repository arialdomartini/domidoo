from sqlalchemy.orm.exc import NoResultFound

from domidooweb.models.base import DBSession
from domidooweb.models.image import Image
from domidooweb.models.tag import Tag


class TagRepository(object):

    def get_or_create_by_name(self, name):
        try:
            return DBSession.query(Tag).filter(Tag.name == name).one()
        except NoResultFound:
            return Tag(name)


    def get_all(self):
        return DBSession.query(Tag).all()


class ImageRepository(object):
    def get(self, id):
        return DBSession.query(Image).filter(Image.id == id).one()

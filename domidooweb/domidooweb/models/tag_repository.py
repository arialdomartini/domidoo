from sqlalchemy.orm.exc import NoResultFound
from domidooweb import DBSession
from domidooweb.models.tag import Tag

__author__ = 'arialdomartini'


class TagRepository(object):

    def get_or_create_by_name(self, name):
        try:
            return DBSession.query(Tag).filter(Tag.name == name).one()
        except NoResultFound:
            return Tag(name)


    def get_all(self):
        return DBSession.query(Tag).all()
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Place,
    )


class PlaceRepository(object):
    def get_first(self):
        return DBSession.query(Place).first()

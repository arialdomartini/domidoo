from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Place,
    )
from domain import PlaceRepository

@view_config(route_name='home', renderer='home.mak')
def home(request):
    repo = PlaceRepository()
    place = repo.get_first()

    return {'place': place}

@view_config(route_name='about', renderer='about.mak')
def about(request):
    return {}




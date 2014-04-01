from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Place,
    )
from domain import PlaceRepository


place_repository = PlaceRepository()

@view_config(route_name='home', renderer='home.mak')
def home(request):
    places = place_repository.get_all()
    return {'places': places}

@view_config(route_name='about', renderer='about.mak')
def about(request):
    return {}

@view_config(route_name='place', renderer='place.mak')
def place(request):
    id = request.matchdict['id']
    place = place_repository.get(id)
    return {'place': place}

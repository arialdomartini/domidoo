from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Place,
    )

@view_config(route_name='admin.home', renderer='admin/home.mak')
def admin_home(request):
    return {}


@view_config(route_name='admin.places.new', renderer='json')
def place_new(request):
    dat = request.json_body
    name = dat['name']
    city = dat['city']
    place = Place(name=name, city=city)
    DBSession.add(place)

    return {'place': dat['name']}

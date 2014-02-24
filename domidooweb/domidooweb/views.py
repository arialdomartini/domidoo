from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    Place,
    )


@view_config(route_name='home', renderer='home.mak')
def home(request):
    return {'project': 'domidooweb'}

@view_config(route_name='about', renderer='about.mak')
def about(request):
    return {}




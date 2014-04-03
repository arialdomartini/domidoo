from pyramid.view import view_config

from domidooweb.models.place_repository import PlaceRepository


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

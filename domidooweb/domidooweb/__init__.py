from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')

    config.add_route('admin.home', '/admin')
    config.add_route('admin.places.new.json', '/admin/places/new.json')
    config.add_route('admin.places.new', '/admin/places/new')

    config.scan()
    return config.make_wsgi_app()

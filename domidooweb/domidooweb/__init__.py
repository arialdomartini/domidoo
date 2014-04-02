from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.paster import setup_logging
from domidooweb.models.base import DBSession, Base


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    if global_config != {}:
        setup_logging(global_config['__file__'])

    config = Configurator(settings=settings)
    config.include('pyramid_mako')


    config.add_static_view(name='images', path=settings['images.uploaded'])
    config.add_static_view('static', 'static', cache_max_age=3600)


    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('place', '/place/{id}')

    config.add_route('admin.home', '/admin')


    config.add_route('admin.places', '/admin/places')
    config.add_route('admin.places.new.json', '/admin/places/new.json')
    config.add_route('admin.places.new', '/admin/places/new')

    config.add_route('admin.tags', '/admin/tags')
    config.add_route('admin.tags.new', '/admin/tags/new')
    config.add_route('admin.tags.add', '/admin/tags/add')

    config.add_route('admin.images.get', '/admin/images/{id}')

    config.scan()
    return config.make_wsgi_app()


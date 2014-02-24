import unittest
import os
import json
from .models import DBSession
from .models import Place

here = os.path.dirname(__file__)
from paste.deploy.loadwsgi import appconfig
dbfile = os.path.join(here, '../db/', 'test.sqlite')

class FunctionalTests(unittest.TestCase):
    def setUp(self):

        from alembic.config import Config
        from alembic import command
        alembic_cfg = Config(os.path.join(here, '../', 'alembic.ini'), ini_section = 'test')
        command.upgrade(alembic_cfg, "head")

        settings = appconfig('config:' + os.path.join(here, '../', 'test.ini'))
        from domidooweb import main
        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def tearDown(self):
        os.unlink(dbfile)


    def test_home(self):
        res = self.testapp.get('/')
        assert res.status == '200 OK'

    def test_about_page_responds(self):
        res = self.testapp.get('/about')
        assert res.status == '200 OK'

    def test_place_new(self):
        res = self.testapp.post_json('/places/new', 
                                     {'name': 'bilocale arredato', 
                                      'city': 'lomazzo'})

        response = json.loads(res.body)

        assert response['place'] == 'bilocale arredato'

        actual = DBSession.query(Place).filter_by(name='bilocale arredato').first()
        assert actual.name == 'bilocale arredato'
        assert actual.city == 'lomazzo'


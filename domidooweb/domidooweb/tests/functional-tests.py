import unittest
import os
import json
from domidooweb.models import DBSession
from domidooweb.models import Place

here = os.path.dirname(__file__)
from paste.deploy.loadwsgi import appconfig
dbfile = os.path.join(here, '../../../../db/', 'test.sqlite')


class FunctionalTests(unittest.TestCase):
    def setUp(self):

        from alembic.config import Config
        from alembic import command
        alembic_cfg = Config(os.path.join(here, '../../', 'alembic.ini'), ini_section = 'test')
        command.upgrade(alembic_cfg, "head")

        settings = appconfig('config:' + os.path.join(here, '../../', 'test.ini'))
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


    def test_that_the_unprotected_admin_page_exists(self):
        res = self.testapp.get('/admin')
        assert res.status == '200 OK'


    def test_a_new_place_with_an_image_can_be_posted(self):

        res = self.testapp.post(url ='/admin/places/new', 
                                params = {'name': 'bilocale arredato', 
                                 'city': 'lomazzo'}, 
                                upload_files = [("image", "example.jpg", "somecontent")]
        )

        assert res.status == '302 Found'

        actual = DBSession.query(Place).filter_by(name='bilocale arredato').first()
        assert actual.name == 'bilocale arredato'
        assert actual.city == 'lomazzo'
        assert actual.image != ""

        upload_dir = '/../../var/tests/images'
        file_path = os.path.join(here, upload_dir, actual.image)

        os.path.isfile(file_path)



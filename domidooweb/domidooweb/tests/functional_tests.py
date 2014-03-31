import unittest
import os
import json
import sure

from domidooweb.models import DBSession


from domidooweb.models import Place
from domidooweb.models import Tag
from domidooweb.models import Image
import transaction

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
        with transaction.manager:
            DBSession.add(Place('name-test', 'city'))

        res = self.testapp.get('/')
        res.status.should.be.equal('200 OK')


    def test_about_page_responds(self):
        res = self.testapp.get('/about')
        res.status.should.be.equal('200 OK')


    def test_that_the_unprotected_admin_page_exists(self):
        res = self.testapp.get('/admin')
        res.status.should.be.equal('200 OK')


    def test_a_new_place_with_an_image_can_be_posted(self):
        res = self.testapp.post(url ='/admin/places/new', 
            params = {'name': 'bilocale arredato', 
                      'city': 'lomazzo'}, 
            upload_files = [("image", "example.jpg", "somecontent")]
        )

        res.status.should.be.equal('302 Found')

        actual = DBSession.query(Place).filter_by(name='bilocale arredato').one()
        actual.name.should.be.equal('bilocale arredato')
        actual.city.should.be.equal('lomazzo')
        actual.images[0].filename.should.contain("example.jpg")

        upload_dir = '../../../../var/tests/images/'
        file_path = os.path.join(here, upload_dir, actual.images[0].filename)
        os.path.isfile(file_path).should.be.true


    def test_a_new_tag_can_be_saved(self):
        res = self.testapp.post(url ='/admin/tags/new', 
            params = {'name': 'bilocale'}
        )

        res.status.should.be.equal('302 Found')

        actual = DBSession.query(Tag).filter_by(name='bilocale').one()
        actual.name.should.be.equal('bilocale')


    def test_a_new_tag_can_be_added_to_a_place(self):
        with transaction.manager:
            place = Place('foo-place', 'city')
            DBSession.add(place)
            placeid = place.id

        res = self.testapp.post(url = '/admin/tags/add', params = {'tag': 'foo', 'place': placeid})

        actual_place = DBSession.query(Place).filter_by(id=placeid).one()
        actual_place.tags[0].name.should.be.equal('foo')


    def test_an_existing_tag_can_be_added_to_a_place(self):
        with transaction.manager:
            existing_tag = Tag(name = 'foo')
            DBSession.add(existing_tag)

            place = Place('foo-place', 'city')
            DBSession.add(place)
            placeid = place.id
            id = existing_tag.id

        res = self.testapp.post(url = '/admin/tags/add', params = {'tag': 'foo', 'place': placeid})

        actual_place = DBSession.query(Place).filter_by(id=placeid).one()
        actual_place.tags[0].name.should.be.equal('foo')


    def test_when_an_existing_tag_is_added_to_a_place_the_tag_is_not_duplicated(self):
        with transaction.manager:
            existing_tag = Tag(name = 'foo')
            DBSession.add(existing_tag)

            place = Place('foo-place', 'city')
            DBSession.add(place)
            placeid = place.id
            id = existing_tag.id

        res = self.testapp.post(url = '/admin/tags/add', params = {'tag': 'foo', 'place': placeid})

        actual_place = DBSession.query(Place).filter_by(id=placeid).one()
        actual_place.tags[0].id.should.be.equal(id)


    def test_a_json_list_of_places_can_be_retrieved(self):
        with transaction.manager:
            DBSession.add(Place(id = 'place1', name = 'foo1', city = 'lomazzo'))
            DBSession.add(Place(id = 'place2', name = 'foo2', city = 'lomazzo'))
            DBSession.add(Place(id = 'place3', name = 'foo3', city = 'lomazzo'))

        res = self.testapp.get(url = '/admin/places')

        actual = res.json_body['places']

        len(actual).should.be.equal(3)
        ids = [p['id'] for p in actual]
        ids.should.contain('place1')
        ids.should.contain('place2')
        ids.should.contain('place3')


    def test_a_json_list_of_all_the_tags_can_be_retrieved(self):
        with transaction.manager:
            DBSession.add(Tag(name = 'foo'))
            DBSession.add(Tag(name = 'bar'))
            DBSession.add(Tag(name = 'foobar baz'))

        res = self.testapp.get(url = '/admin/tags')

        actual = res.json_body['tags']

        len(actual).should.be.equal(3)
        tag_names = [ tag['name'] for tag in actual ]
        tag_names.should.contain('foo')
        tag_names.should.contain('bar')
        tag_names.should.contain('foobar baz')


    def test_an_image_can_be_retrieved_by_id(self):
        with transaction.manager:
            place = Place(name = "foo", city = "NY")
            image = Image(filename = 'foo.png', place = place)
            DBSession.add(image)
            image_id = image.id

        res = self.testapp.get(url = '/admin/images/{id}'.format(id = image_id))
        
        actual = res.json_body

        actual['image']['filename'].should.be.equal('foo.png')

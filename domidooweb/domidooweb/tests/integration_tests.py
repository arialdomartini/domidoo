import unittest

from pyramid import testing
from mock import Mock

from domidooweb.models.base import *
import domidooweb.views
from domidooweb.admin.admin_views import *


dburl = 'sqlite://'
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        
        DBSession.remove()

        engine = create_engine(dburl)
        
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        self.request = testing.DummyRequest()


    def tearDown(self):
        DBSession.remove()
        testing.tearDown()


    def test_that_about_page_can_be_reached(self):
        info = domidooweb.views.about(self.request)

        assert True

    def test_home_displays_the_list_of_all_places(self):
        place_repository = Mock(PlaceRepository)
        domidooweb.views.place_repository = place_repository
        place_repository.get_all.return_value = {'place1', 'place2', 'place3'}

        response = domidooweb.views.home(self.request)
        places = response['places']

        len(places).should.be.equal(3)


    def test_show_a_single_place(self):
        place_repository = Mock(PlaceRepository)
        domidooweb.views.place_repository = place_repository
        place = Place(name = 'foo', city = 'Milan', id = 'abda-78782')
        place_repository.get.return_value = place
        self.request.matchdict['id'] = 'abda-78782'
        response = domidooweb.views.place(self.request)

        response['place'].id.should.be.equal('abda-78782')






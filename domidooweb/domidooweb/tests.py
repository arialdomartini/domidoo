import unittest
import transaction
import os
from pyramid import testing

from .models import *
from .views import *
from .admin_views import *

dburl = 'sqlite://'
class IntegrationTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        
        DBSession.remove()

        engine = create_engine(dburl)
        from .models import (
            Base,
            Place,
            )
        
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        self.request = testing.DummyRequest()


    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_that_home_can_be_reached(self):
        info = home(self.request)

        assert info['project'] == 'domidooweb'

    def test_that_about_page_can_be_reached(self):
        info = about(self.request)

        assert True


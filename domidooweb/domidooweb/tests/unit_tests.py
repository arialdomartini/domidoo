import unittest
import sure

from domidooweb.models import Place

class FunctionalTests(unittest.TestCase):
    def test_place_id_should_be_created_if_missing(self):
        place = Place(name = 'foo', city = 'lomazzo', image = None)

        assert place.id != None

    def test_place_id_can_be_programmatically_specified(self):
        place = Place(id = 'myid', name = 'foo', city = 'lomazzo', image = None)

        place.id.should.be.equal('myid')

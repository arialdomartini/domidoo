import unittest
import sure

from domidooweb.models import Tag
from domidooweb.models import Place

class ModelTests(unittest.TestCase):
    def test_tag_has_a_unique_autogenerated_id(self):
        tag1 = Tag("foo")
        tag2 = Tag("bar")
        tag1.id.shouldnt.be.equal(tag2.id)

    def test_place_id_should_be_created_if_missing(self):
        place = Place(name = 'foo', city = 'lomazzo', image = None)

        assert place.id != None

    def test_place_id_can_be_programmatically_specified(self):
        place = Place(id = 'myid', name = 'foo', city = 'lomazzo', image = None)

        place.id.should.be.equal('myid')

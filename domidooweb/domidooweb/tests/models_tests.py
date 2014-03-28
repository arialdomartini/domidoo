import unittest
import sure
import json

from domidooweb.models import Tag
from domidooweb.models import Place
from domidooweb.models import Image

class ModelsTests(unittest.TestCase):
    def test_tags_have_unique_autogenerated_ids(self):
        tag1 = Tag("foo")
        tag2 = Tag("bar")
        tag1.id.shouldnt.be.equal(tag2.id)

    def test_places_have_unique_autogenerated_ids(self):
        place1 = Place(name = 'foo1', city = 'bar1')
        place2 = Place(name = 'foo2', city = 'bar2')
        place1.id.shouldnt.be.equal(place2.id)

    def test_place_id_should_be_created_if_missing(self):
        place = Place(name = 'foo', city = 'lomazzo')

        assert place.id != None

    def test_place_id_can_be_programmatically_specified(self):
        place = Place(id = 'myid', name = 'foo', city = 'lomazzo')

        place.id.should.be.equal('myid')

    def test_images_have_unique_autogenerated_ids(self):
        image1 = Image(filename = 'foo1', place = None)
        image2 = Image(filename = 'foo2', place = None)
        image1.id.shouldnt.be.equal(image2.id)

    def test_an_image_can_be_json_serialized(self):
        image = Image(filename = "some_filename.jpg", place = None)

        actual = image.to_json()

        actual['filename'].should.be.equal("some_filename.jpg")

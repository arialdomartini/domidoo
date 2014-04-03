from domidooweb import DBSession
from domidooweb.models.image import Image
from domidooweb.models.image_repository import ImageRepository
from domidooweb.models.place import Place
from domidooweb.tests.integration_tests import IntegrationTests
import sure

__author__ = 'arialdomartini'


class ImageRepositoryTests(IntegrationTests):

    def test_an_iname_can_be_retrieved_by_by_id(self):
        place = Place(name = "foo", city = "bar")
        image=Image(filename = 'foobar', place = place)
        DBSession.add(image)

        sut = ImageRepository()

        actual = sut.get(image.id)

        actual.filename.should.be.equal('foobar')
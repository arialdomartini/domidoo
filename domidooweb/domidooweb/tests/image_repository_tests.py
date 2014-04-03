from domidooweb.admin.admin_views import *
from domidooweb.models.image import Image
from integration_tests import IntegrationTests 

from domidooweb.domain import ImageRepository


class ImageRepositoryTests(IntegrationTests):

    def test_an_iname_can_be_retrieved_by_by_id(self):
        place = Place(name = "foo", city = "bar")
        image=Image(filename = 'foobar', place = place)
        DBSession.add(image)

        sut = ImageRepository()

        actual = sut.get(image.id)

        actual.filename.should.be.equal('foobar')

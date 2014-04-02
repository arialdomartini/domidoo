import unittest
import transaction
import os
from pyramid import testing

from domidooweb.allmodels import *
from domidooweb.views import *
from domidooweb.admin_views import *
from integration_tests import IntegrationTests 

from domidooweb.domain import ImageRepository
from domidooweb.allmodels import Image

class ImageRepositoryTests(IntegrationTests):

    def test_an_iname_can_be_retrieved_by_by_id(self):
        place = Place(name = "foo", city = "bar")
        image=Image(filename = 'foobar', place = place)
        DBSession.add(image)

        sut = ImageRepository()

        actual = sut.get(image.id)

        actual.filename.should.be.equal('foobar')
